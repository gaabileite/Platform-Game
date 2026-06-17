class GameOver:
    def __init__(self, state):
        self.state = state

    def update(self):
        surface.fill(game_over_bg)

        title_text = font_title.render("GAME OVER", True, background_color)
        surface.blit(title_text, title_text.get_rect(center=(internal_width // 2, internal_height // 2 - 15)))

        subtitle_text = font_subtitle.render("Press SPACE to reset", True, player_color)
        surface.blit(subtitle_text, subtitle_text.get_rect(center=(internal_width // 2, internal_height // 2 + 15)))

        if keys[K_SPACE]:
            self.state = False
