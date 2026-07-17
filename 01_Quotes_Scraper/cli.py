"""
CLI MODULE
Professional terminal UI for all scraping projects.
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.rule import Rule
from rich import box
from datetime import datetime

console = Console()


def show_banner():

    console.print(
        Panel.fit(
            "[bold cyan]📚 QUOTES SCRAPER v1.0[/bold cyan]",
            border_style="green",
        )
    )


def show_project_info(
    website: str,
    delay: str,
    outputs: str,
):

    table = Table(
        title="Project Information",
        box=box.ROUNDED,
        border_style="cyan"
    )

    table.add_column("Property", style="yellow", no_wrap=True)
    table.add_column("Value", style="white")

    table.add_row("Website", website)
    table.add_row("Delay", delay)
    table.add_row("Outputs", outputs)
    table.add_row(
        "Started",
        datetime.now().strftime("%I:%M:%S %p")
    )

    console.print(table)


def page_header(page_number: int):

    console.print()
    console.print(
        Rule(f"[bold blue]PAGE {page_number}[/bold blue]")
    )


def show_page_stats(
    page_quotes: int,
    total_quotes: int
):

    table = Table(
        box=box.MINIMAL_DOUBLE_HEAD
    )

    table.add_column("Statistic", style="green")
    table.add_column("Value", style="white")

    table.add_row(
        "Quotes This Page",
        str(page_quotes)
    )

    table.add_row(
        "Total Quotes",
        str(total_quotes)
    )

    console.print(table)


def show_waiting(seconds: float):

    console.print(
        f"[yellow]⏳ Waiting {seconds:.1f} sec...[/yellow]"
    )


def success(message: str):

    console.print(
        f"[bold green]✔ {message}[/bold green]"
    )


def error(message: str):

    console.print(
        f"[bold red]✖ {message}[/bold red]"
    )


def show_summary(
    pages: int,
    quotes: int,
    elapsed: float,
):

    table = Table(
        title="Scraping Summary",
        box=box.ROUNDED,
        border_style="green"
    )

    table.add_column("Item", style="cyan")
    table.add_column("Value", style="white")

    table.add_row("Pages Scraped", str(pages))
    table.add_row("Quotes Scraped", str(quotes))
    table.add_row("JSON", "✔")
    table.add_row("CSV", "✔")
    table.add_row("Excel", "✔")
    table.add_row(
        "Execution Time",
        f"{elapsed:.2f} sec"
    )

    console.print(table)

    console.print(
        "[bold green]🎉 Scraping Completed Successfully![/bold green]"
    )