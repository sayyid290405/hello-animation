import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Warna
black = (0, 0, 0)
white = (255, 255, 255)

# Mengatur font
font = pygame.font.Font(None, 74)  # Ukuran font 74
text = font.render('Hello kontol', True, white)  # Membuat surface untuk teks
text_rect = text.get_rect(center=(100, screen_height // 2))  # Posisi awal teks

# Kecepatan gerakan
speed = 5

# Loop utama
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Menggerakkan teks
    text_rect.x += speed

    # Jika teks keluar dari layar, reset posisi
    if text_rect.x > screen_width:
        text_rect.x = -text_rect.width  # Reset ke kiri layar

    # Menggambar latar belakang dan teks
    screen.fill(black)
    screen.blit(text, text_rect)

    # Memperbarui tampilan
    pygame.display.flip()
    pygame.time.delay(20)  # Delay untuk mengatur kecepatan animasi