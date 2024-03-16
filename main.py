
import sys
import matplotlib

import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 9999

df = pd.read_csv('Sprzedaż 2023 [Kopia] - 2023.csv')




# df.plot(x = 'Kategoria', y = 'Suma jm.')
# df['Data'].plot(kind = 'hist')

df.plot()
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
