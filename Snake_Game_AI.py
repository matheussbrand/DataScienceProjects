import pygame  # Importa o módulo pygame para criar o jogo
import random  # Importa o módulo random para gerar números aleatórios
import sys  # Importa o módulo sys para interagir com o sistema
import numpy as np  # Importa o módulo numpy para operações matemáticas
from keras.models import Sequential  # Importa a classe Sequential do Keras para criar modelos sequenciais
from keras.layers import Dense  # Importa a classe Dense do Keras para criar camadas densas
from keras.utils import to_categorical  # Importa a função to_categorical do Keras para conversão de dados
from keras.callbacks import TensorBoard  # Importa a classe TensorBoard do Keras para callbacks de TensorBoard

# Constantes
WIDTH, HEIGHT = 600, 400  # Define a largura e altura da tela do jogo
SNAKE_SIZE = 10  # Define o tamanho da serpente
SNAKE_SPEED = 15  # Define a velocidade inicial da serpente
WHITE = (255, 255, 255)  # Define a cor branca em RGB
BLACK = (0, 0, 0)  # Define a cor preta em RGB
RED = (255, 0, 0)  # Define a cor vermelha em RGB
ORANGE = (255, 165, 0)  # Define a cor laranja em RGB

pygame.init()  # Inicializa o Pygame

game_display = pygame.display.set_mode((WIDTH, HEIGHT))  # Define o tamanho da tela do jogo
pygame.display.set_caption("Snake Game")  # Define o título da janela do jogo

clock = pygame.time.Clock()  # Cria um objeto Clock para controlar a taxa de atualização da tela

message_font = pygame.font.SysFont("ubuntu", 30)  # Define a fonte para mensagens no jogo
score_font = pygame.font.SysFont("ubuntu", 30)  # Define a fonte para exibir a pontuação

# Modelo de IA
model = Sequential()  # Cria um modelo sequencial
model.add(Dense(64, activation="relu", input_dim=4))  # Adiciona uma camada densa com ativação ReLU e 64 neurônios de entrada
model.add(Dense(64, activation="relu"))  # Adiciona uma segunda camada densa com ativação ReLU e 64 neurônios
model.add(Dense(4, activation="softmax"))  # Adiciona uma camada densa de saída com ativação softmax e 4 neurônios
model.compile(loss="categorical_crossentropy", optimizer="adam")  # Compila o modelo com a função de perda e otimizador especificados

# Callback do TensorBoard
tensorboard = TensorBoard(
    log_dir="logs", histogram_freq=0, write_graph=True, write_images=True
)  # Define o callback TensorBoard com os parâmetros especificados


def print_score(score, last_score): # Define uma função para exibir a pontuação na tela do jogo
    current_score_text = score_font.render("Score: " + str(score), True, ORANGE)
    last_score_text = score_font.render("Last Score: " + str(last_score), True, ORANGE)
    game_display.blit(current_score_text, [10, 10])
    game_display.blit(last_score_text, [10, 40])


def draw_snake(snake_size, snake_pixels): # Define uma função para desenhar a serpente na tela do jogo
    for pixel in snake_pixels:
        pygame.draw.rect(
            game_display, WHITE, [pixel[0], pixel[1], snake_size, snake_size]
        )


def game_over_screen(score, last_score): # Define uma função para exibir a tela de fim de jogo
    game_display.fill(BLACK)
    game_over_message = message_font.render("Game Over! Press Enter.", True, RED)
    game_display.blit(game_over_message, [WIDTH / 6, HEIGHT / 3])
    print_score(score, last_score)
    pygame.display.update()


def run_game(): # Define a função principal que executa o jogo
    last_score = 0
    snake_length = 1
    snake_speed = SNAKE_SPEED

    x, y = WIDTH / 2, HEIGHT / 2
    x_speed, y_speed = 0, 0

    snake_pixels = []
    target_x, target_y = (
        random.randint(0, WIDTH - SNAKE_SIZE) // 10 * 10,
        random.randint(0, HEIGHT - SNAKE_SIZE) // 10 * 10,
    )

    # Inicia o buffer de experiencia
    experience_buffer = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    snake_length = 1
                    snake_speed = SNAKE_SPEED
                    x, y = WIDTH / 2, HEIGHT / 2
                    x_speed, y_speed = 1, 1
                    snake_pixels = []
                    target_x, target_y = (
                        random.randint(0, WIDTH - SNAKE_SIZE) // 10 * 10,
                        random.randint(0, HEIGHT - SNAKE_SIZE) // 10 * 10,
                    )

        # Decisão da IA
        state = np.array([x, y, target_x, target_y])
        action_probs = model.predict(state.reshape(1, 4))
        action = np.argmax(action_probs)

        if action == 0:  # Left
            x_speed = -SNAKE_SIZE
            y_speed = 0
        elif action == 1:  # Right
            x_speed = SNAKE_SIZE
            y_speed = 0
        elif action == 2:  # Up
            x_speed = 0
            y_speed = -SNAKE_SIZE
        elif action == 3:  # Down
            x_speed = 0
            y_speed = SNAKE_SIZE

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_over_screen(snake_length - 1, last_score)
            last_score = max(last_score, snake_length - 1)
            snake_length = 1
            snake_speed = SNAKE_SPEED
            x, y = WIDTH / 2, HEIGHT / 2
            x_speed, y_speed = 0, 0
            snake_pixels = []
            target_x, target_y = (
                random.randint(0, WIDTH - SNAKE_SIZE) // 10 * 10,
                random.randint(0, HEIGHT - SNAKE_SIZE) // 10 * 10,
            )

        x += x_speed
        y += y_speed

        game_display.fill(BLACK)
        pygame.draw.rect(
            game_display, ORANGE, [target_x, target_y, SNAKE_SIZE, SNAKE_SIZE]
        )

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_over_screen(snake_length - 1, last_score)
                last_score = max(last_score, snake_length - 1)
                snake_length = 1
                snake_speed = SNAKE_SPEED
                x, y = WIDTH / 2, HEIGHT / 2
                x_speed, y_speed = 0, 0
                snake_pixels = []
                target_x, target_y = (
                    random.randint(0, WIDTH - SNAKE_SIZE) // 10 * 10,
                    random.randint(0, HEIGHT - SNAKE_SIZE) // 10 * 10,
                )

        draw_snake(SNAKE_SIZE, snake_pixels)
        print_score(snake_length - 1, last_score)

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x, target_y = (
                random.randint(0, WIDTH - SNAKE_SIZE) // 10 * 10,
                random.randint(0, HEIGHT - SNAKE_SIZE) // 10 * 10,
            )
            snake_length += 1
            if snake_length % 5 == 0:
                snake_speed += 1

        # Store experience in buffer
        experience_buffer.append((state, action, snake_length - 1, target_x, target_y))

        # Train model every 1000 steps
        if len(experience_buffer) > 1000:
            experiences = random.sample(experience_buffer, 100000)
            states, actions, rewards, next_states, next_actions = zip(*experiences)
            states = np.array(states)
            actions = to_categorical(actions, num_classes=4)
            rewards = np.array(rewards)
            next_states = np.array(next_states)
            next_actions = to_categorical(next_actions, num_classes=10)
            model.fit(states, actions, epochs=1, callbacks=[tensorboard])

        clock.tick(snake_speed)


run_game()  # Chama a função principal para iniciar o jogo
