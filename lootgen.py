from rich.console import Console
from rich.table import Table
import random
import sys

console = Console()
RARE_PROB = 0.05

def simulate_loot(num_chests: int = 100, rare_prob: float = RARE_PROB) -> int:
    """Симулирует выпадение редкого лута."""
    rare_count = sum(1 for _ in range(num_chests) if random.random() < rare_prob)
    return rare_count

def main():
    num_chests = 100
    if len(sys.argv) > 1:
        try:
            num_chests = int(sys.argv[1])
        except ValueError:
            console.print("[red]Ошибка: укажите число сундуков как аргумент[/red]")
            sys.exit(1)

    rare = simulate_loot(num_chests)

    table = Table(title="LootGen — Симуляция лута")
    table.add_column("Параметр", style="cyan")
    table.add_column("Значение", style="magenta")
    table.add_row("Количество сундуков", str(num_chests))
    table.add_row("Вероятность редкого предмета", f"{RARE_PROB*100}%")
    table.add_row("Выпало редких предметов", str(rare))

    console.print(table)

if __name__ == "__main__":
    main()
