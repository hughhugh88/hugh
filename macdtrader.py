import backtrader as bt
import datetime
import backtrader.feeds as btfeeds

total = 0
times = 0
opportunities = []

tickers = ['MMM', 'AOS', 'ABT', 'ABBV', 'ACN', 'ADBE', 'AMD', 'AES', 'AFL', 'A', 'APD', 'ABNB', 'AKAM', 'ALB', 'ARE', 'ALGN', 'ALLE', 'LNT', 'ALL', 'GOOG', 'MO', 'AMZN', 'AMCR', 'AEE', 'AAL', 'AEP', 'AXP', 'AIG', 
           'AMT', 'AWK', 'AMP', 'AME', 'AMGN', 'APH', 'ADI', 'ANSS', 'AON', 'APA', 'AAPL', 'AMAT', 'APTV', 'ACGL', 'ADM', 'ANET', 'AJG', 'AIZ', 'T', 'ATO', 
           'ADSK', 'ADP', 'AZO', 'AVB', 'AVY', 'AXON', 'BKR', 'BALL', 'BAC', 'BK', 'BBWI', 'BAX', 'BDX', 'BBY', 'BIO', 'TECH', 'BIIB', 'BLK', 'BX', 'BA', 
           'BKNG', 'BWA', 'BSX', 'BMY', 'AVGO', 'BR', 'BRO', 'BLDR', 'BG', 'BXP', 'CHRW', 'CDNS', 'CZR', 'CPT', 'CPB', 'COF', 'CAH', 'KMX', 'CCL', 'CARR', 
           'CTLT', 'CAT', 'CBOE', 'CBRE', 'CDW', 'CE', 'COR', 'CNC', 'CNP', 'CF', 'CRL', 'SCHW', 'CHTR', 'CVX', 'CMG', 'CB', 'CHD', 'CI', 'CINF', 'CTAS', 
           'CSCO', 'C', 'CFG', 'CLX', 'CME', 'CMS', 'KO', 'CTSH', 'CL', 'CMCSA', 'CAG', 'COP', 'ED', 'STZ', 'CEG', 'COO', 'CPRT', 'GLW', 'CPAY', 'CTVA', 
           'CSGP', 'COST', 'CTRA', 'CRWD', 'CCI', 'CSX', 'CMI', 'CVS', 'DHR', 'DRI', 'DVA', 'DAY', 'DECK', 'DE', 'DAL', 'DVN', 'DXCM', 'FANG', 'DLR', 'DFS', 
           'DG', 'DLTR', 'D', 'DPZ', 'DOV', 'DOW', 'DHI', 'DTE', 'DUK', 'DD', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'ELV', 'EMR', 'ENPH', 'ETR', 
           'EOG', 'EPAM', 'EQT', 'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'ETSY', 'EG', 'EVRG', 'ES', 'EXC', 'EXPE', 'EXPD', 'EXR', 'XOM', 'FFIV', 'FDS', 'FICO', 
           'FAST', 'FRT', 'FDX', 'FIS', 'FITB', 'FSLR', 'FE', 'FI', 'FMC', 'F', 'FTNT', 'FTV', 'FOXA', 'FOX', 'BEN', 'FCX', 'GRMN', 'IT', 'GE', 'GEHC', 'GEN', 
           'GNRC', 'GD', 'GIS', 'GM', 'GPC', 'GILD', 'GPN', 'GL', 'GDDY', 'GS', 'HAL', 'HIG', 'HAS', 'HCA', 'DOC', 'HSIC', 'HSY', 'HES', 'HPE', 'HLT', 'HOLX', 
           'HD', 'HON', 'HRL', 'HST', 'HWM', 'HPQ', 'HUBB', 'HUM', 'HBAN', 'HII', 'IBM', 'IEX', 'IDXX', 'ITW', 'INCY', 'IR', 'PODD', 'INTC', 'ICE', 'IFF', 
           'IP', 'IPG', 'INTU', 'ISRG', 'IVZ', 'INVH', 'IQV', 'IRM', 'JBHT', 'JBL', 'JKHY', 'J', 'JNJ', 'JCI', 'JPM', 'JNPR', 'K', 'KVUE', 'KDP', 'KEY', 
           'KEYS', 'KMB', 'KIM', 'KMI', 'KKR', 'KLAC', 'KHC', 'KR', 'LHX', 'LH', 'LRCX', 'LW', 'LVS', 'LDOS', 'LEN', 'LLY', 'LIN', 'LYV', 'LKQ', 'LMT', 'L', 
           'LOW', 'LULU', 'LYB', 'MTB', 'MRO', 'MPC', 'MKTX', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MTCH', 'MKC', 'MCD', 'MCK', 'MDT', 'MRK', 'META', 'MET', 
           'MTD', 'MGM', 'MCHP', 'MU', 'MSFT', 'MAA', 'MRNA', 'MHK', 'MOH', 'TAP', 'MDLZ', 'MPWR', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MSCI', 'NDAQ', 'NTAP', 
           'NFLX', 'NEM', 'NWSA', 'NWS', 'NEE', 'NKE', 'NI', 'NDSN', 'NSC', 'NTRS', 'NOC', 'NCLH', 'NRG', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ORLY', 'OXY', 'ODFL', 
           'OMC', 'ON', 'OKE', 'ORCL', 'OTIS', 'PCAR', 'PKG', 'PANW', 'PARA', 'PH', 'PAYX', 'PAYC', 'PYPL', 'PNR', 'PEP', 'PFE', 'PCG', 'PM', 'PSX', 'PNW', 
           'PNC', 'POOL', 'PPG', 'PPL', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PTC', 'PSA', 'PHM', 'QRVO', 'PWR', 'QCOM', 'DGX', 'RL', 'RJF', 'RTX', 'O', 
           'REG', 'REGN', 'RF', 'RSG', 'RMD', 'RVTY', 'ROK', 'ROL', 'ROP', 'ROST', 'RCL', 'SPGI', 'CRM', 'SBAC', 'SLB', 'STX', 'SRE', 'NOW', 'SHW', 'SPG', 
           'SWKS', 'SJM', 'SNA', 'SO', 'LUV', 'SWK', 'SBUX', 'STT', 'STLD', 'STE', 'SYK', 'SMCI', 'SYF', 'SNPS', 'SYY', 'TMUS', 'TROW', 'TTWO', 
           'TPR', 'TRGP', 'TGT', 'TEL', 'TDY', 'TFX', 'TER', 'TSLA', 'TXN', 'TXT', 'TMO', 'TJX', 'TSCO', 'TT', 'TDG', 'TRV', 'TRMB', 'TFC', 'TYL', 'TSN', 
           'USB', 'UBER', 'UDR', 'ULTA', 'UNP', 'UAL', 'UPS', 'URI', 'UNH', 'UHS', 'VLO', 'VTR', 'VRSN', 'VRSK', 'VZ', 'VRTX', 'VTRS', 'VICI', 'V', 'VST', 
           'VMC', 'WRB', 'GWW', 'WAB', 'WBA', 'WMT', 'DIS', 'WBD', 'WM', 'WAT', 'WEC', 'WFC', 'WELL', 'WST', 'WDC', 'WY', 'WMB', 'WTW', 'WYNN', 'XEL', 'XYL', 
           'YUM', 'ZBRA', 'ZBH', 'ZTS']
#tickers = ['MMM','AOS','ABT']
for ticker in tickers:

    cerebro = bt.Cerebro()

    cerebro.broker.set_cash(10000)

    data = btfeeds.GenericCSVData(
        dataname = 'backtest/data/sp500/4h/{}4h.csv'.format(ticker),
        fromdate = datetime.datetime(2024, 6, 30),
        todate = datetime.datetime(2024, 9, 18),
        reverse = False
    )

    cerebro.adddata(data)

    class TestStrategy(bt.Strategy):

        params = (
            # Standard MACD Parameters
            ('macd1', 55),
            ('macd2', 89),
            ('macdsig', 10),
            ('atrperiod', 14),  # ATR Period (standard)
            ('atrdist', 3.0),   # ATR distance for stop price
            ('smaperiod', 30),  # SMA Period (pretty standard)
            ('dirperiod', 10),  # Lookback period to consider SMA trend direction
            ('longperiod', 61),
            ('rsi_period', 14),
            ('overbought', 60),
        )
        def log(self, txt, dt=None):
            ''' Logging function for this strategy'''
            dt = dt or self.datas[0].datetime.date(0)
            print('%s, %s' % (dt.isoformat(), txt))

        def __init__(self):
            self.macd = bt.indicators.MACD(self.data,
                                        period_me1=self.p.macd1,
                                        period_me2=self.p.macd2,
                                        period_signal=self.p.macdsig)

            # Cross of macd.macd and macd.signal
            self.mcross = bt.indicators.CrossOver(self.macd.macd, self.macd.signal)

            # To set the stop price
            self.atr = bt.indicators.ATR(self.data, period=self.p.atrperiod)

            # Control market trend
            self.sma = bt.indicators.SMA(self.data, period=self.p.smaperiod)
            self.smadir = self.sma - self.sma(-self.p.dirperiod)
            self.longsma = bt.indicators.SMA(self.data, period=self.p.longperiod)

            self.rsi = bt.indicators.RSI(period=self.params.rsi_period)

        def start(self):
            # Keep a reference to the "close" line in the data[0] dataseries
            self.dataclose = self.datas[0].close
            self.order = None

        def notify_order(self, order):
            if order.status in [order.Submitted, order.Accepted]:
                return
            
            if order.status in [order.Completed]:
                if order.isbuy():
                    self.log('BUY EXECUTED {}'.format(order.executed.price))
                elif order.issell():
                    self.log('SELL EXECUTED {}'.format(order.executed.price))

            self.order = None
                    
        def next(self):
            if self.order:
                return  # pending order execution

            if not self.position:  # not in the market
                if self.mcross[0] > 0.0:
                    self.order = self.buy()
                    pdist = self.atr[0] * self.p.atrdist
                    self.pstop = self.data.close[0] - pdist
                    print('{}'.format(ticker))
                    opportunities.append(ticker)
        
            elif self.rsi > self.params.overbought:
                if ticker in opportunities:
                    opportunities.remove(ticker)

            else:  # in the market
                if self.mcross[0] < 0.0:
                    self.close()


    cerebro.addstrategy(TestStrategy)

    cerebro.addsizer(bt.sizers.AllInSizer, percents = 50)
    #cerebro.addsizer(backtrader.sizers.FixedSize, stake = 100)

    #print('{}'.format(ticker))
    #print('Starting Porfolio Value: %.2f' % cerebro.broker.getvalue())
    
    cerebro.run()

    #print('Final Portfolio Vaule: %.2f' % cerebro.broker.getvalue())

    times = times + 1

    total = total + cerebro.broker.getvalue()



print(total/times)
print(opportunities)