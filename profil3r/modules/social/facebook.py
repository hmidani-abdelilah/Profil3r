import requests
from profil3r.colors import Colors
import time

class Facebook:

    def __init__(self, config, permutations_list):
        # 500 ms
        self.delay = 500 / 1000
        # https://facebook.com/{username}
        self.format = config['plateform']['facebook']['format']
        # facebook usernames are not case sensitive
        self.permutations_list = [perm.lower() for perm in permutations_list]

    # Generate all potential facebook usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        print(Colors.BOLD + Colors.OKGREEN + "\n----- FACEBOOK -----\n" + Colors.ENDC)

        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username)
            except requests.ConnectionError:
                print("failed to connect to facebook")
            
            # If the account exists
            if r.status_code == 200:
                print(Colors.BOLD + "[+] " + Colors.ENDC + Colors.HEADER  + username + Colors.ENDC)
            
            time.sleep(self.delay)