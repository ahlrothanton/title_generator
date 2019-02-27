#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class TitleGenerator:
    """generate yourself a title"""

    def __init__(self, prefixes=['Cloud', 'Devops', 'SRE', 'System'], suffixes=['Consultant', 'Engineer', 'Architect', 'Developer', 'Specialist', 'Wizard', 'Ninja']):
        if prefixes is not None:
            self.prefixes = prefixes

        if suffixes is not None:
            self.suffixes = suffixes

        import random
        if bool(random.getrandbits(1)):
            self.title = 'Senior '
        else:
            self.title = ''
        self.title += random.choice(self.prefixes)  + ' ' + random.choice(self.suffixes)

if __name__ == "__main__":
    # use the default titles
    print(TitleGenerator().title)

    # use custom titles
    prefixes = ['AI', 'Blockchain', 'Cloud']
    suffixes = ['Developer', 'Architect']
    print(TitleGenerator(prefixes, suffixes).title)
