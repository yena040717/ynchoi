import os
import pickle

file_path = 'score.bin'

def save_scores(scores, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(scores, file)

def load_scores(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            scores = pickle.load(file)
            return scores
    return None

loaded_scores = load_scores(file_path)

if loaded_scores is not None:
    print('[파일 읽기]')
    scores = loaded_scores
else:
    scores = []
    print('[점수 입력]')
    while True:
        n = int(input(f'#{len(scores) + 1}? '))
        if n < 0:
            break
        scores.append(n)

    if scores:
        save_scores(scores, file_path)

if scores:
    print('\n[점수 출력]')
    print('개인점수:', ' '.join(map(str, scores)))
    avg = sum(scores) / len(scores)
    print(f'평균: {avg:.1f}')
