import glob, os, time, sys
import pandas as pd

files = sorted(glob.glob(os.path.join("q1", "data_Q1_2024", "*.csv")))
print("pandas", pd.__version__)
print("files:", len(files))

start = time.time()
frames, rows = [], 0
for i, f in enumerate(files, 1):
    df = pd.read_csv(f, low_memory=False)
    frames.append(df)
    rows += len(df)
    print("[%d/%d] %s  rows=%s  elapsed=%.1fs" % (i, len(files), os.path.basename(f), format(rows, ","), time.time()-start), flush=True)

big = pd.concat(frames, ignore_index=True)
print("LOADED", big.shape, "in %.1fs" % (time.time()-start))
print("memory GB:", big.memory_usage(deep=True).sum() / 1e9)
