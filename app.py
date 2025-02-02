"""Main entrypoint of the udpater tool.
Only useable for an already installed modpack."""

from rich.console import Console
from rich.prompt import Prompt
import toml

# Charger la configuration
def load_config():
    with open('config.toml', 'r') as file:
        config = toml.load(file)
    return config['modpacks']

# Afficher le menu et sélectionner un modpack
def select_modpack():
    modpacks = load_config()
    console = Console()
    console.print("[bold]Sélectionnez un modpack à mettre à jour:[/bold]")
    for key, value in modpacks.items():
        console.print(f"{key}: {value}")
    selected = Prompt.ask("Entrez le numéro du modpack", choices=list(modpacks.keys()))
    return modpacks[selected]

def main() -> None:
    selected_modpack = select_modpack()
    print(f"Modpack sélectionné : {selected_modpack}")

if __name__ == "__main__":
    main()