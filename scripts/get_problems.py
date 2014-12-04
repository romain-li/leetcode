#!/usr/bin/env python

import os
import re
import json

from pyquery import PyQuery as pyq
import html2text

PROBLEMS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'problems')


def getProblems():
    """ Get problem list from leetcode problems page """
    doc = pyq(url='https://oj.leetcode.com/problems/')
    problems = doc('#problemList tr')
    for problem in problems:
        problem = pyq(problem)
        a = problem('td:eq(1) a')
        title = a.text()
        url = 'https://oj.leetcode.com/%s' % a.attr('href')
        add_date = problem('td:eq(2)').text()
        difficulty = problem('td:eq(4)').text()
        book = True if problem('i.fa-book') else False
        getProblem(title, url, add_date, difficulty, book)


def getProblem(title, url, add_date='', difficulty='', book=False):
    """ Get problem detail information from problem url """
    # Skip the problem with book icon because I can't get the detail page
    if book:
        return

    # Skip the exists problems
    problem_dir = os.path.join(PROBLEMS_DIR, title.replace(' ', '_'))
    if os.path.exists(problem_dir):
        return

    # Make problem dir and init the code
    os.mkdir(problem_dir)

    # Get problem content
    print 'Fetching problem: %s ...' % title
    doc = pyq(url=url)
    html = doc('.question-content').remove('#tags').remove('.hide').html()
    problem = html2text.html2text(html)
    code = getCode(doc('form.container div.row:eq(1) > div:first').attr('ng-init'))

    # Write informations
    with open(os.path.join(problem_dir, '__init__.py'), 'w') as f:
        writeLine(f, 'TITLE = \'%s\'' % title)
        writeLine(f, 'ADD_DATE = \'%s\'' % add_date)
        writeLine(f, 'DIFFICULTY = \'%s\'' % difficulty)
        writeLine(f, 'URL = \'%s\'' % url)
        writeLine(f, 'BOOK = %s' % book)
        writeLine(f, 'PROBLEM = r"""%s\n"""' % problem)

    with open(os.path.join(problem_dir, 'solution.py'), 'w') as f:
        f.write(code)


def getCode(init_code, lang='python'):
    """ Get the default code from angular script """
    m = re.match('init\((\[.*),\]', init_code)
    if m:
        codes = json.loads(m.group(1).replace('\'', '"') + ']')
        for item in codes:
            if item.get('value') == lang:
                return item.get('defaultCode')


def writeLine(fd, s, encode='utf-8'):
    """ Write and encode the string """
    fd.write(s.encode(encode))
    fd.write('\n')

if __name__ == '__main__':
    getProblems()
