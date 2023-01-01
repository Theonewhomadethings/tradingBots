# region imports
from AlgorithmImports import *
# endregion

class CrawlingSkyBlueCoyote(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2015, 9, 1)  # Set Start Date
        self.SetEndDate(2021, 10, 1) #set end date
        self.SetCash(100000)  # Set Strategy Cash
        #self.AddEquity("SPY", Resolution.Minute)
        #self.AddEquity("BND", Resolution.Minute)
        #self.AddEquity("AAPL", Resolution.Minute)
        self.AddRiskManagement(TrailingStopRiskManagementModel(0.05))
        tickerList = ['PBCT', 'XEC', 'PCL', 'FLT', 'SBNY', 'ALLE', 'IR', 'MLM', 'EXR', 'INCY', 'CDNS', 'FTI', 'WU', 'IPGP', 'TSG', 'CEPH', 'KMX', 'SIG', 'ARNC', 'AMCR', 'ETSY', 'CRL', 'CELG', 'BBBY', 'ESS', 'TRMB', 'FANG', 'HCA', 'FRE', 'VTR', 'COV', 'ARG', 'TIE', 'MGM', 'REG', 'WB', 'ITT', 'LEG', 'KHC', 'AJG', 'ILMN', 'IEX', 'WPX', 'IT', 'HRL', 'USL', 'CMCSK', 'HPE', 'DXCM', 'MON', 'BWA', 'ZTS', 'DWDP', 'FAST', 'MOS', 'GOOGL', 'INFO', 'CCK', 'NDSN', 'HOT', 'MMI', 'HOG', 'CLF', 'CHD', 'TWX', 'MAA', 'ADS', 'BMC', 'FFIV', 'RAD', 'DPS', 'NFLX', 'FTV', 'DJ', 'PCLN', 'TYC', 'SAI', 'CMG', 'UA/UAA', 'PNR', 'DFS', 'SMS', 'GGP', 'JBL', 'PCP', 'TDY', 'RSH', 'ALB', 'FDS', 'NCR', 'NOVL', 'CPGX', 'VNT', 'AYE', 'ODP', 'MNK', 'M', 'HNZ', 'BXLT', 'CBE', 'CARR', 'DLPH', 'GM', 'MIL', 'AVP', 'PENN', 'ON', 'DYN', 'BCR', 'THC', 'CPWR', 'CBOE', 'WYN', 'ALXN', 'FDC', 'FL', 'LLL', 'SUN', 'SEDG', 'STZ', 'SIVB', 'FRT', 'TEL', 'DG', 'COO', 'SWY', 'AN', 'NWS', 'CEG', 'CDAY', 'TSO', 'TRGP', 'CXO', 'CZR', 'TRB', 'FRC', 'TE', 'FRX', 'GNW', 'TDC', 'NOV', 'HSP', 'HAR', 'MOLX', 'KMI', 'KORS', 'TIF', 'YHOO', 'GT', 'NE', 'XLNX', 'UHS', 'JOY', 'PGN', 'VICI', 'TSLA', 'CSGP', 'AA', 'IDXX', 'WST', 'FLR', 'SCG', 'HSIC', 'AKS', 'MTCH', 'PCS', 'KSS', 'VAR', 'FHN', 'PLL', 'DNR', 'JDSU', 'WLP', 'FOX', 'ABBV', 'WCG', 'NFX', 'GPN', 'TRIP', 'DISH', 'AAL', 'STI','EXPE', 'NBL', 'HBI', 'CPT', 'VIAB', 'MHK', 'EMC', 'GRE', 'RCL', 'LKQ', 'MBI', 'EVHC', 'AMD', 
'MXIM', 'DELL', 'V', 'CDW', 'FBHS', 'TYL', 'MAC', 'EK', 'GENZ', 'NOW', 'OMX', 'CERN', 'MUR', 'PCG', 'SNI', 'MTD', 'MOH', 'ODFL', 'MFE', 'STLD', 'ULTA', 'TER', 'EPAM', 'VRSK', 'TLAB', 'SLG', 'TFX', 'QEP', 'ANF', 'PYPL', 'STJ', 'CA', 'NYT', 'PAYC', 'NAVI', 'XYL', 'LUK', 'WAB', 'FLIR', 'JWN', 'TSS', 'CFC', 'CAM', 'CHK', 'MNST', 'ARE', 'KEYS', 'CVC', 'PRGO', 'X', 'GPS', 'FSR', 
'BIO', 'EW', 'JEF', 'OTIS', 'GNRC', 'ESRX', 'UAL', 'BJS', 'RE', 'GRA', 'GAS', 'DV', 'CPRT', 'RIG', 'HII', 'ROL', 'NCLH', 'DD', 'FB', 'LSI', 'TDG', 'AMG', 'WRB', 'DNB', 'MRNA', 'S', 'BS', 'TWTR', 'T', 'DLTR', 'PKG', 'CE', 'CIEN', 'ENDP', 'JKHY', 'CCE', 'AWK', 'CTLT', 'AOS', 'EQT', 'CTX', 'GMCR', 'SNPS', 'PTC', 'AYI', 'PDCO', 'MKTX', 'AV', 'OGN', 'RDC', 'SNDK', 'LRCX', 'GRMN', 'AET', 'SLR', 'DOW', 'ALGN', 'URI', 'STE', 'SWN', 'FLS', 'FII', 'URBN', 'CNX', 'AGN', 'EP', 
'CSC', 'INVH', 'DF', 'STX', 'WIN', 'LEH', 'LDW', 'AIV', 'HFC', 'RTN', 'POOL', 'JNPR', 'CVG', 'SBAC', 'TMC', 'TMUS', 'ENPH', 'CTVA', 'JBHT', 'SII', 'JEC', 'GLK', 'SGP', 'GHC', 'HCBK', 'WFM', 'QTRN', 'APC', 'DISCK', 'KSU', 'DPZ', 'UDR', 'XTO', 'PSX', 'ABK', 'KDP', 'BHF', 'VNO', 'INTU', 'ADT', 'EQIX', 'EVRG', 'ANR', 'AVGO', 'HWM', 'PBI', 'FOXA', 'SBL', 'ANSS', 'LYV', 'LXK', 'BC', 'KBH', 'MHS', 'CFN', 'UAA', 'ICE', 'XRX', 'RRD', 'CVH', 'NLSN', 'CTXS', 'BIG', 'ATI', 'MJN', 'GR', 'SBUX', 'DLR', 'POM', 'SWKS', 'TGNA', 'LIFE', 'OI', 'LVLT', 'LDOS', 'NKTR', 'R', 'RMD', 'KRFT', 'ZBRA', 'RJF', 'ATVI', 'DO', 'ROST', 'FDO', 'BTU', 'HFI', 'LNT', 'KSE', 'TEG', 'O', 'QRVO', 'VRTX', 'CCL', 'SIAL', 'FOSL', 'NYX', 'BRO', 'FMC', 'JNS', 'SHLD', 'CPRI', 'CRM', 'ACE', 'AVB', 'SRCL', 'ALTR', 'FTR', 'ETFC', 'HOLX', 'AME', 'MAT', 'ANDV', 'IGT', 'REGN', 'ACN', 
'CNC', 'HRS', 'SLE', 'UNM', 'WLTW', 'SE', 'COL', 'NXPI', 'DRE', 'MBC', 'BLK', 'CB', 'LO', 'MPC', 'GME', 'PETM', 'RAI', 'RHT', 'APOL', 'BRCM', 'AAP', 'HRB', 'RX', 'SLM', 'CFG', 'MSCI', 'JCP', 'AMZN', 'SVU', 'BMS', 'HLT', 'JNY', 'ABMD', 'ANET', 'NVR', 'MWW', 'FTNT', 'TWC', 'NVLS', 'GEHC', 'CHTR', 'LVS', 'FNM', 'RRC', 'KG', 'MPWR', 'COTY', 'UA', 'NSM', 'MI', 'NBR', 'SYF', 'ACAS', 'TTWO', 'TECH', 'DXC', 'COG', 'WFR', 'ACGL', 'ATO', 'PVH', 'KFT', 'MEE', 'BR', 'STR', 'CSRA', 'LM', 'SPLS', 'DTV', 'Q', 'HP', 'LW', 'FSLR', 'PTV', 'CCI', 'LYB', 'DAL', 'BEAM', 'LLTC', 
'XL', 'ESV', 'ABS', 'TSCO', 'ALK']
#quant connect differentiates between symbols and tickers
        for ticker in tickerList:
            self.AddEquity(ticker, Resolution.Hour)
        
        self.change = self.AddData(SPXChange, "change", Resolution.Hour).Symbol




    def OnData(self, data: Slice):
        if self.change in data:
            targets = []
            for ticker in data[self.change].Added:
                if ticker in data:
                    targets.append(PortfolioTarget(ticker, 0.1))
            for ticker in data[self.change].Removed:
                if ticker in data:
                    targets.append(PortfolioTarget(ticker, -0.05))
            self.SetHoldings(targets)

class SPXChange(PythonData):
    def getSource(self, config, date, isLive):
        source = "https://www.dropbox.com/s/ksi5liwjja8fxzv/SPYChanges.csv?dl=0"
        return SubscriptionDataSource(source, SubscriptionTransportMedium.RemoteFile)

    def Reader(self, config, line, date, isLive):
        if not (line.strip() and line[0].isdigit()):
            return None
        data = line.split(",")
        change = SPXChange()

        try:
            change.Symbol = config.Symbol
            change.Time = datetime.strptime(data[0], "%Y-%m-%d") + timedelta(hours=10)
            change.Value = 0
            change["Added"] = str(data[1]).split(" ")
            change["Removed"] = str(data[2]).split(" ")
        except ValueError:
            return None
        return change
