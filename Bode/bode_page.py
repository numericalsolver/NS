import flet as ft
from flet import *

def bode(page: Page):
    page.title = "BODE PLOT"
    page.bgcolor = '#E6F4F1'

    # Define top navigation row
    top_nav = ft.Container(
        Text("BODE PLOT", size=20, weight=FontWeight.BOLD),
        bgcolor='#1D818C',
        width=1920,
    )

    # Define content for each section
    section1 = Column(
        controls=[
            Text(
                "What is Bode Plot",
                size=20,
                weight=FontWeight.BOLD,
                color='#000000',
            ),
            Image(src=f"\assets\bode_sec1.png",
                           width=100,
                           height=100,
                           fit=ft.ImageFit.CONTAIN,
            ),
            Text(
                "A Bode plot illustrates how a signal changes when passing through a system across a frequency range."
                "It displays the magnitude and phase of a transfer function as frequencies vary."
                "To effectively represent a wide frequency range and magnitudes, we employ a logarithmic scale for frequency and magnitude, using decibels (dB) for magnitude measurements."
                "This approach ensures comprehensive representation and clarity in understanding the system's behaviour.",
                color='#000000',
            ),
            Icon(name=icons.INFO, color=colors.BLUE_GREY),
        ],
    )

    section2 = Column(
        controls=[
            Text(
                "Why do we use Bode plot",
                size=20,
                weight=FontWeight.BOLD,
                color='#000000',
            ),
            Text(
                "Bode plots provide valuable insights into the behavior of a system at different "
                "frequencies. They help engineers understand stability, gain margin, phase margin, and "
                "frequency response characteristics of the system.",
                color='#000000',
            ),
            Icon(name=icons.ABC, color=colors.ORANGE),
        ],
    )

    section3 = Column(
        expand=1, wrap=False, scroll="always",
        controls=[
            Text(
                "Where do we use Bode plot",
                size=20,
                weight=FontWeight.BOLD,
            ),
            Text(
                "Bode plots are used in various fields including control system design, signal processing, "
                "communications, and electronics. They are particularly useful in analyzing feedback "
                "systems and designing filters.",
                color='#000000',
            ),
            Icon(name=icons.ABC, color=colors.GREEN),
        ],
    )

    section4 = Column(
        controls=[
            Text(
                "How it works",
                size=20,
                weight=FontWeight.BOLD,
            ),
            Text(
                "Bode plot works by plotting the magnitude and phase of the transfer function of a system "
                "against frequency on a logarithmic scale. This allows engineers to visualize the frequency "
                "response characteristics and identify critical points such as resonant frequencies and "
                "crossover frequencies.",
            ),
            Text(
                "BODE PLOTTER",
            ),
            
        ],
    )

    # Define the layout of the website
    website_layout = Column(
        controls=[top_nav, section1, section2, section3, section4],
        height="100%",
        width="100%",
    )

    # Add the website layout to the page
    page.add(website_layout)

# Run the application
ft.app(target=bode, view=WEB_BROWSER)
