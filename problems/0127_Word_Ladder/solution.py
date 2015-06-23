import Queue


class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        word_dict = set(wordDict)
        word_dict.add(beginWord)
        word_dict.add(endWord)
        # Prepare word nodes
        word_node_dict = {}
        word_change_map = {}
        for word in word_dict:
            word_node = Word(word)
            for i in range(len(word)):
                key = word[0:i] + '?' + word[i + 1:]
                word_change_map.setdefault(key, set())
                change_map = word_change_map.get(key)
                for other_word_node in change_map:
                    word_node.add_neighbor(other_word_node)
                    other_word_node.add_neighbor(word_node)
                change_map.add(word_node)

            word_node_dict[word] = word_node

        # Solution
        begin_word = word_node_dict.get(beginWord)
        end_word = word_node_dict.get(endWord)
        visited_words = set()
        word_queue = Queue.Queue()
        word_queue.put((begin_word, 0))
        while not word_queue.empty():
            word, distance = word_queue.get()
            distance += 1
            if word == end_word:
                return distance
            if word not in visited_words:
                visited_words.add(word)
                for neighbor in word.get_neighbors():
                    word_queue.put((neighbor, distance))
        return 0

class Word(object):
    def __init__(self, word):
        self._word = word
        self._neighbors = set()

    def get_neighbors(self):
        return self._neighbors

    def add_neighbor(self, word):
        self._neighbors.add(word)

    def __repr__(self):
        return self._word

    def __str__(self):
        return self._word
