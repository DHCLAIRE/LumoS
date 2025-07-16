#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from itertools import cycle

class DialogueManager:
    def __init__(self, path="prompts/questions.json"):
        with open(path, 'r', encoding='utf-8') as f:
            self.questions = json.load(f)
        self.iterator = cycle(self.questions)
        self.current = next(self.iterator)

    def get_next(self):
        self.current = next(self.iterator)
        return self.current['text']
