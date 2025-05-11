import numpy as np
import pandas as pd

def simulate_efold(fold_scores, alpha=0.05):
    records = []
    stop_fold = None
    
    for n in range(1, len(fold_scores) + 1):
        current_scores = fold_scores[:n]
        mean_score = np.mean(current_scores)
        
        if n == 1:
            ci_width = None
            delta_ci = None
            stop = False
        else:
            ci_width_prev = ci_width
            std_err = np.std(current_scores, ddof=1) / np.sqrt(n)
            ci_width = 2 * 1.96 * std_err
            delta_ci = abs(ci_width_prev - ci_width)
            threshold = alpha * ci_width
            stop = delta_ci <= threshold
            if stop:
              stop_msg = f"Yes ({round(delta_ci, 3)} ≤ {round(threshold, 5)})"
            else:
              stop_msg = False
            if stop and stop_fold is None:
              stop_fold = n

        records.append({
            "Fold": n,
            "Mean NDCG@10": round(mean_score, 3),
            "CI Width": round(ci_width, 3) if ci_width else None,
            "ΔCI": round(delta_ci, 3) if delta_ci else None,
            "Stop?": stop_msg if n > 1 else None
          })

        if stop:
            break

    return pd.DataFrame(records), stop_fold, mean_score
