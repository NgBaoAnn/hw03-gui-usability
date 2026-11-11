"""Calculate SUS from genuine response CSV; missing data never becomes zero."""
import argparse
import csv
import json
import statistics
from pathlib import Path


def score(values):
    if len(values) != 10 or any(type(v) is not int or not 1 <= v <= 5 for v in values):
        raise ValueError('SUS requires exactly ten integer responses in [1, 5]')
    return sum(v - 1 if i % 2 == 0 else 5 - v for i, v in enumerate(values)) * 2.5


def analyse(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as stream:
        rows = list(csv.DictReader(stream))
    if len(rows) != 7 or {r['participant_id'] for r in rows} != {f'P{i}' for i in range(1, 8)}:
        raise ValueError('Expected seven distinct participants P1-P7; pilot is excluded')
    results = []
    for row in rows:
        try:
            responses = [int(row[f'q{i}']) for i in range(1, 11)]
        except (KeyError, ValueError) as error:
            raise ValueError(f"{row['participant_id']}: missing/invalid SUS responses") from error
        results.append({'participant_id': row['participant_id'], 'sus': score(responses)})
    return {'participants': results, 'n': 7, 'mean_sus': statistics.mean(r['sus'] for r in results)}


def self_check():
    assert score([3] * 10) == 50
    assert score([5, 1] * 5) == 100
    assert score([1, 5] * 5) == 0
    assert score([1] * 10) == 50
    for invalid in [[], [1] * 9, [0] * 10, [6] * 10, [1.5] * 10, [True] * 10]:
        try:
            score(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError(f'Accepted invalid responses: {invalid}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv', nargs='?')
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()
    if args.test:
        self_check()
        print('SUS self-check passed: endpoints, neutral responses and invalid inputs')
    elif args.csv:
        try:
            print(json.dumps(analyse(args.csv), ensure_ascii=False, indent=2))
        except ValueError as error:
            parser.exit(2, f'No analysis produced: {error}\n')
    else:
        parser.error('Provide response CSV or --test')
