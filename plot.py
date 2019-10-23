from baselines_merl.common import plot_util as pu
import matplotlib.pyplot as plt


results = pu.load_results('path/to/your/experiment01')

pu.plot_results(results, average_group=True,
                split_fn=lambda _: '', shaded_std=False, shaded_err=True,
                figsize=(10, 6), smooth_step=10.0)

plt.title('Experiment01', fontsize=30)

plt.tight_layout()
plt.show()
