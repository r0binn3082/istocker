import matplotlib.pyplot as plt

def plot_seasonal_diff(df, columns, start_date, end_date,lags=7):
    """
    Function to visualize original series vs lagged series and their difference.
    Useful for checking stationarity and seasonality in stock data.
    """
    # 1. حساب الفرق (Differencing) للفترة المحددة
    diff_data = df[columns].diff(lags)[start_date:end_date]
    
    # 2. إنشاء الشكل (Figure)
    fig, axs = plt.subplots(2, 1, sharex=True, figsize=(10, 7))
    
    # الرسمة الأولى: البيانات الأصلية والبيانات المُزاحة (Lagged)
    df[columns][start_date:end_date].plot(ax=axs[0], legend=True, marker=".", alpha=0.7)
    df[columns][start_date:end_date].shift(lags).plot(ax=axs[0], grid=True, legend=False, linestyle=":", alpha=0.5)
    axs[0].set_title(f"Original Series vs {lags}-Day Lag")
    axs[0].set_ylabel("Value")
    
    # الرسمة الثانية: الفرق (The Difference)
    diff_data.plot(ax=axs[1], grid=True, marker=".", color=['orange', 'green'])
    axs[1].set_title(f"{lags}-Day Difference (Seasonality Removed)")
    axs[1].set_ylabel("Difference")
    
    plt.tight_layout()
    plt.show()