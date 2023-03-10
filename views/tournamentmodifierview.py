"""View : View for the Tournament Modification Module of the Tournaments Controller."""

from views.abcview import View


class TournamentModifierView(View):
    """View for the Tournament Modification Module."""
    def __init__(self):
        """Menus prompts are declared here."""
        self.PROMPT_FOR_FIRST_TURN_CREATION = ("Voulez-vous générer un premier tour pour le tournoi ?\n"
                                               "1 - Taper n'importe quelle touche pour OUI\n"
                                               "2 - Taper 2 ou R pour NON et retourner au Menu des tournois\n")
        self.PROMPT_FOR_TURN_CREATION = ("Voulez-vous générer un nouveau tour pour le tournoi ?\n"
                                         "1 - Taper n'importe quelle touche pour OUI\n"
                                         "2 - Taper 2 ou R pour NON et retourner au Menu des tournois\n")

    def prompt_for_match_winner(self, match):
        """Prompt for the winner of a match"""
        prompt = (f"Saisir le gagnant du match :\n"
                  f"1 - {str(match[0][0])}\n"
                  f"2 - {str(match[1][0])}\n"
                  f"3 - Match nul\n"
                  f"4 - Revenir au Menu des tournois\n")
        match_winner = self.get_correct_input(prompt, ["1", "2", "3", "4"])
        return match_winner

    def prompt_for_turn_creation(self, new=False):
        """Ask if the user wants to generate a new turn now or return to menu."""
        if new:
            prompt = self.PROMPT_FOR_FIRST_TURN_CREATION
        else:
            prompt = self.PROMPT_FOR_TURN_CREATION
        create = input(prompt)
        if create == "r" or create == "R" or create == "2":
            return None
        else:
            return create

    @View.pretty_print_decorator
    def print_tournament_details(self, tournament):
        """Display all the information of a tournament in a readable way."""
        print(repr(tournament))
