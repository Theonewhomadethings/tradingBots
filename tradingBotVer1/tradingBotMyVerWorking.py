import numpy as np
from AlgorithmImports import *


class WellDressedFluorescentYellowFrog(QCAlgorithm):

    def Initialize(self):
        # Set the cash for backtest
        self.SetCash(100000)
        
        # Start and end dates for backtest
        self.SetStartDate(2017,9,1)
        self.SetEndDate(2020,9,1)
        
        # Add asset
        self.symbol = self.AddEquity("SPY", Resolution.Daily).Symbol
        
        # Lookback length for b/o (in days)
        self.lookback = 20
        
        # Upper/lower limit for lookback length
        self.ceiling, self.floor = 30, 10
        
        # Price offset for stop order
        self.initialStopRisk = 0.98
        self.trailingStopRisk = 0.9
        
        # Schedule function 20 minutes after every market open
        self.Schedule.On(self.DateRules.EveryDay(self.symbol), \
                        self.TimeRules.AfterMarketOpen(self.symbol, 20), \
                        Action(self.EveryMarketOpen))


    def OnData(self, data):
        # Plot security's price
        self.Plot("Data Chart", self.symbol, self.Securities[self.symbol].Close)

 
    def EveryMarketOpen(self):
        # Dynamically determine lookback length based on 30 day volatility change rate
        close = self.History(self.symbol, 31, Resolution.Daily)["close"]
        todayvol = np.std(close[1:31])
        yesterdayvol = np.std(close[0:30])
        deltavol = (todayvol - yesterdayvol) / todayvol
        self.lookback = round(self.lookback * (1 + deltavol))
        
        # Account for upper/lower limit of lockback length
        if self.lookback > self.ceiling:
            self.lookback = self.ceiling
        elif self.lookback < self.floor:
            self.lookback = self.floor
        
        # List of daily highs
        self.high = self.History(self.symbol, self.lookback, Resolution.Daily)["high"]
        
        # Buy in case of breakout
        if not self.Securities[self.symbol].Invested and \
                self.Securities[self.symbol].Close >= max(self.high[:-1]):
            self.SetHoldings(self.symbol, 1)
            self.breakoutlvl = max(self.high[:-1])
            self.highestPrice = self.breakoutlvl
        
        
        # Create trailing stop loss if invested 
        if self.Securities[self.symbol].Invested:
            
            # If no order exists, send stop-loss
            if not self.Transactions.GetOpenOrders(self.symbol):
                self.stopMarketTicket = self.StopMarketOrder(self.symbol, \
                                        -self.Portfolio[self.symbol].Quantity, \
                                        self.initialStopRisk * self.breakoutlvl)
            
            # Check if the asset's price is higher than highestPrice & trailing stop price not below initial stop price
            if self.Securities[self.symbol].Close > self.highestPrice and \
                    self.initialStopRisk * self.breakoutlvl < self.Securities[self.symbol].Close * self.trailingStopRisk:
                # Save the new high to highestPrice
                self.highestPrice = self.Securities[self.symbol].Close
                # Update the stop price
                updateFields = UpdateOrderFields()
                updateFields.StopPrice = self.Securities[self.symbol].Close * self.trailingStopRisk
                self.stopMarketTicket.Update(updateFields)
                
                # Print the new stop price with Debug()
                self.Debug(updateFields.StopPrice)
            
            # Plot trailing stop's price
            self.Plot("Data Chart", "Stop Price", self.stopMarketTicket.Get(OrderField.StopPrice))
