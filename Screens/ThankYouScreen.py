from manim import *

class ThankYouScreen(Scene):
    def construct(self):
        # Thank You Text
        thank_you_text = Text("Thank You!", font_size=72, color=BLUE)
        # Subtitle
        subtitle = Text("For Your Attention", font_size=36, color=WHITE).next_to(thank_you_text, DOWN, buff=0.5)
        
        # Animations
        self.play(Write(thank_you_text))
        self.wait(1)
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(8)  # Hold on the screen for 8 seconds

        # Fade Out
        self.play(FadeOut(thank_you_text, scale=0.8), FadeOut(subtitle, scale=0.8))
