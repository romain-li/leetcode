#!/usr/bin/env python

import os
import re
import json
import shutil

from pyquery import PyQuery as PyQ
import html2text

PROBLEMS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'problems')


def get_problems():
    """ Get problem list from leetcode problems page """
    doc = PyQ(url='https://oj.leetcode.com/problems/')
    problems = doc('#problemList tbody tr')
    for problem in problems:
        problem = PyQ(problem)
        _id = int(problem('td:eq(1)').text())
        a = problem('td:eq(2) a')
        title = a.text()
        url = 'https://oj.leetcode.com/%s' % a.attr('href').lstrip('/')
        difficulty = problem('td:eq(4)').text()
        book = True if problem('i.fa-book') else False
        get_problem(title, _id, url, difficulty, book)


def get_problem(title, _id, url, difficulty='', book=False):
    """ Get problem detail information from problem url """
    # Skip the problem with book icon because I can't get the detail page
    if book:
        return

    # Skip the exists problems
    problem_dir = os.path.join(PROBLEMS_DIR, '%.4d_%s' % (_id, title.replace(' ', '_')))
    if os.path.exists(problem_dir):
        return

    # Make problem dir and init the code
    os.mkdir(problem_dir)

    # Get problem content
    print 'Fetching problem: %s ...' % problem_dir
    doc = PyQ(url=url)
    _html = doc('.question-content').remove('#tags').remove('.hide').html()
    problem = html2text.html2text(_html)
    code = get_code(doc('form.container div.row:eq(1) > div:first').attr('ng-init'))

    # Write information
    with open(os.path.join(problem_dir, '__init__.py'), 'w') as f:
        write_line(f, 'ID = \'%d\'' % _id)
        write_line(f, 'TITLE = \'%s\'' % title)
        write_line(f, 'DIFFICULTY = \'%s\'' % difficulty)
        write_line(f, 'URL = \'%s\'' % url)
        write_line(f, 'BOOK = %s' % book)
        write_line(f, 'PROBLEM = r"""%s\n"""' % problem)

    with open(os.path.join(problem_dir, 'solution.py'), 'w') as f:
        f.write(code)

    shutil.copy(os.path.join(PROBLEMS_DIR, '.default', 'test.py'),
                os.path.join(problem_dir, 'test.py'))


def get_code(init_code, lang='python'):
    """ Get the default code from angular script """
    m = re.match('init\((\[.*),\]', init_code)
    if m:
        codes = json.loads(m.group(1).replace('\'', '"') + ']')
        for item in codes:
            if item.get('value') == lang:
                return item.get('defaultCode')


def write_line(fd, s, encode='utf-8'):
    """ Write and encode the string """
    fd.write(s.encode(encode))
    fd.write('\n')

if __name__ == '__main__':
    get_problems()
