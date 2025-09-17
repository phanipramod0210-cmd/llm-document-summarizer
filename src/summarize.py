import argparse

def fallback_summarize(text, n=3):
    s = text.replace('\n',' ').split('.')
    return '.'.join([seg.strip() for seg in s[:n] if seg.strip()]) + '.'

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--file', required=True)
    args=p.parse_args()
    with open(args.file) as f:
        txt=f.read()
    print('SUMMARY:\n')
    print(fallback_summarize(txt))
