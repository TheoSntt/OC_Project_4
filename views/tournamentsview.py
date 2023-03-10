"""View : View for the Tournaments Manager SubController."""

from views.abcview import View


class TournamentsView(View):
    """View for the Tournaments Manager SubController."""
    def __init__(self):
        """Menus prompts are declared here."""
        self.MAIN_MENU_PROMPT = ("Que voulez-vous faire ?\n"
                                 "1 - Lister tous les tournois\n"
                                 "2 - Créer un tournoi\n"
                                 "3 - Continuer un tournoi en cours\n"
                                 "4 - Retour au Menu principal\n")
        self.MAIN_MENU_VALUES = ["1", "2", "3", "4"]

        self.SELECTOR_MENU_PROMPT = ("Selectionnez un tournoi pour voir les options \n"
                                     "R - Retour au menu précédent\n"
                                     "A - Retour au Menu Principal\n")
        self.SELECTOR_MENU_VALUES = ["R", "A", "r", "a"]

        self.TOURNAMENT_OPTIONS_PROMPT = ("Tournoi sélectionné :\n"
                                          "<>\n"
                                          "1 - Lister les participants par ordre alphabétique\n"
                                          "2 - Afficher toutes les informations sur le tournoi\n"
                                          "3 - Retour au menu des tournois\n")
        self.TOURNAMENT_OPTIONS_VALUES = ["1", "2", "3"]

        self.TOURNAMENT_MODIFYING_OPTIONS_PROMPT = ("Tournoi sélectionné :\n"
                                                    "<>\n"
                                                    "1 - Continuer la saisie des tours\n"
                                                    "2 - Retour au menu des tournois\n")
        self.TOURNAMENT_MODIFYING_OPTIONS_VALUES = ["1", "2"]

    def prompt_main_menu(self):
        """Prompt the Tournaments Manager Main Menu."""
        user_choice = self.get_correct_input(self.MAIN_MENU_PROMPT, self.MAIN_MENU_VALUES)
        return user_choice

    def prompt_selector_menu(self, number_of_tournaments):
        """Prompt the tournament selector menu. Allow to select a tournament in the displayed list."""
        values = self.SELECTOR_MENU_VALUES
        for i in range(1, number_of_tournaments+1):
            values.append(str(i))
        # print(values)
        user_choice = self.get_correct_input(self.SELECTOR_MENU_PROMPT, values)
        return user_choice

    def prompt_tournament_options(self, tournament_string):
        """Prompt the tournament options menu. Once a tournament is selected, display the options."""
        user_choice = self.get_correct_input(self.TOURNAMENT_OPTIONS_PROMPT.replace("<>", tournament_string),
                                             self.TOURNAMENT_OPTIONS_VALUES)
        return user_choice

    def prompt_tournament_modifying_options(self, tournament_string):
        """Prompt the tournament modifying options menu. Once a tournament is selected, display the options."""
        user_choice = self.get_correct_input(self.TOURNAMENT_MODIFYING_OPTIONS_PROMPT.replace("<>", tournament_string),
                                             self.TOURNAMENT_MODIFYING_OPTIONS_VALUES)
        return user_choice

    @View.pretty_print_decorator
    def print_tournaments_for_selection(self, tournaments_list, in_progress=False):
        """List all tournaments, with numbering to allow the user to select one in the list."""
        tournaments_list.sort(key=lambda x: x.start_date)
        if in_progress:
            print("LISTE DE TOUS LES TOURNOIS EN COURS")
        else:
            print("LISTE DE TOUS LES TOURNOIS ENREGISTRES DANS L'APPLICATION")
        print()
        i = 1
        for tournament in tournaments_list:
            print(f"{i} - {tournament}")
            i += 1

    @View.pretty_print_decorator
    def print_tournament_details(self, tournament):
        """Display all the information of a tournament in a readable way."""
        print(repr(tournament))

    @View.pretty_print_decorator
    def print_all_players(self, player_list, show_detail=False):
        """Display a list of all players, in a compact or detailed way."""
        if show_detail:
            player_list.sort(key=lambda x: x.surname)
            print("LISTE DE TOUS LES JOUEURS DU TOURNOI")
            print()
            for player in player_list:
                print(repr(player))
                print()
        else:
            player_list.sort(key=lambda x: x.surname)
            print("LISTE DE TOUS LES JOUEURS DU TOURNOI")
            print()
            for player in player_list:
                print(player)
