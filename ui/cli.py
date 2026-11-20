from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

from core.harness import Harness


class CLI:
    def __init__(self):
        self.console = Console()

    def show_banner(self):
        title = Text("CALUDE CODE ;)", style="bold bright_cyan")
        subtitle = Text("Your local coding harness", style="white")
        content = Text.assemble(title, "\n", subtitle)

        self.console.print()
        self.console.print(
            Panel(
                Align.center(content),
                border_style="bright_blue",
                padding=(1, 4),
            )
        )
        self.console.print(
            "[dim]Type your request and press Enter. Type [bold]exit[/bold] or "
            "[bold]quit[/bold] to close.[/dim]"
        )
        self.console.print()

    def run(self):
        self.show_banner()
        harness = Harness()

        while True:
            try:
                user_input = Prompt.ask("[bold bright_cyan]You[/bold bright_cyan]")
            except (EOFError, KeyboardInterrupt):
                self.console.print("\n[dim]Session closed.[/dim]")
                break

            if user_input.strip().lower() in {"exit", "quit"}:
                self.console.print("[dim]Session closed. See you next time![/dim]")
                break

            if not user_input.strip():
                self.console.print("[yellow]Please enter a request.[/yellow]")
                continue

            self.console.print()
            harness.run(user_input)
            self.console.print()
