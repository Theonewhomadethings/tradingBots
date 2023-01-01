# region imports
from AlgorithmImports import *
# endregion

class CrawlingSkyBlueCoyote(QCAlgorithm):
    def Initialize(self):

        self.SetStartDate(2015, 9, 1)  # Set Start Date
        self.SetEndDate(2021, 10, 1) # Set End Date
        self.SetCash(100000)  # Set Strategy Cash
        
        self.AddRiskManagement(TrailingStopRiskManagementModel(0.05))
        
        tickerList = ['PCG',  'CMCSK',  'MHS',  'GPN',  'CHD',  'T',  'CCK',  'FOXA',  'SYF',  'AMD',  'TLAB',  'PETM',  'LEH',  'STJ',  'ANF',  'FBHS',  'TSG',  'FDO',  'AMZN',  'LYB',  'PSX',  'TRIP',  'X',  'SMS',  'EQIX',  'VTR',  'OI',  'WLTW',  'NVR',  'JEF',  'COV',  'FLS',  'KFT',  'PLL',  'RRD',  'CA',  'MAT',  'FL',  'MTD',  'MSCI',  'MEE',  'FDC',  'TECH',  'MFE',  'MON',  'SWN',  'LEG',  'ODFL',  'AWK',  'ANR',  'LYV',  'PAYC',  'CPRI',  'ESRX',  'DLTR',  'CSRA',  'NDSN',  'TIF',  'BCR',  'EPAM',  'HAR',  'JCP',  'V',  'DOW',  'FRX',  'MKTX',  'BRO',  'CAM',  'APOL',  'WYN',  'UHS',  'JWN',  'TSCO',  'TMC',  'HOT',  'TSO',  'PVH',  'VAR',  'MAA',  'RAI',  'DXC',  'RMD',  'ATVI',  'RIG',  'R',  'FMC',  'ALK',  'BHF',  'SWKS',  'QEP',  'FOSL',  'JNPR',  'TTWO',  'STR',  'AET',  'IEX',  'MOH',  'FRE',  'CEPH',  'PRGO',  'KMI',  'DG',  'DLPH',  'TDG',  'SBAC',  'ALLE',  'CNC',  'ABMD',  'KSS',  'CBE',  'CTX',  'USL',  'CFN',  'WU',  'HPE',  'TEL',  'PCL',  'DRE',  'IR',  'PCLN',  'RDC',  'SBNY',  'DNB',  'TSLA',  'BIG',  'LRCX',  'TYC',  'BTU',  'LNT',  'XRX',  'KG',  'DWDP',  'ALB',  'CDAY',  'GMCR',  'BWA',  'FLIR',  'BXLT',  'DISH',  'RAD',  'ICE',  'AV',  'NFLX',  'BMC',  'REG',  'DF',  'TYL',  'ETFC',  'GOOGL',  'FFIV',  'NLSN',  'SLR',  'CFG',  'FDS',  'XYL',  'HBI',  'CIEN',  'ESS',  'EQT',  'RCL',  'HRL',  'PNR',  'GNW',  'LXK',  'MIL',  'NBR',  'CPRT',  'HSIC',  'DTV',  'CBOE',  'PCS',  'TRMB',  'MGM',  'EP',  'SBUX',  'YHOO',  'AAP',  'HWM',  'CZR',  'OMX',  'COTY',  'NCLH',  'LIFE',  'FII',  'LDOS',  'TGNA',  'PYPL',  'VRSK',  'BEAM',  'SEDG',  'LW',  'BIO',  'TRB',  'CCE',  'HSP',  'TMUS',  'CPWR',  'LLTC',  'MUR',  'TER',  'NSM',  'UNM',  'CHK',  'CVG',  'WB',  'LDW',  'AMCR',  'NCR',  'ABS',  'CTLT',  'GME',  'AN',  'PTC',  'GENZ',  'CHTR',  'SBL',  'APC',  'JBHT',  'SCG',  'HOG',  'CMG',  'ILMN',  'BR',  'ITT',  'LSI',  'SIAL',  'BRCM',  'RRC',  'COG',  'ZTS',  'HFC',  'JBL',  'DYN',  'SWY',  'NAVI',  'HCA',  'Q',  'FTI',  'SHLD',  'STE',  'TE',  'TIE',  'JEC',  'GGP',  'WST',  'CCI',  'KORS',  'COO',  'VRTX',  'SLG',  'EXPE',  'ROL',  'JNY',  'KMX',  'PENN',  'CVC',  'AJG',  'WIN',  'UDR',  'UAA',  'INFO',  'MRNA',  'HNZ',  'CPT',  'O',  'CB',  'FLT',  'COL',  'DJ',  'DXCM',  'STX',  'WPX',  'GRA',  'MOS',  'NOW',  'UA',  'UAL',  'SUN',  'ZBRA',  'FHN',  'PGN',  'CNX',  'ULTA',  'CSC',  'GNRC',  'MI',  'NFX',  'VNT',  'SAI',  'ALTR',  'XLNX',  'ACN',  'MLM',  'DLR',  'HLT',  'ANET',  'NWS',  'GHC',  'BBBY',  'AMG',  'BMS',  'JNS',  'PCP',  'FAST',  'CDW',  'EVRG',  'SNI',  'STZ',  'MTCH',  'PKG',  'MBI',  'ABK',  'IPGP',  'ARNC',  'QRVO',  'BS',  'EVHC',  'BJS',  'MWW',  'TEG',  'RJF',  'SLM',  'TFX',  'AOS',  'SIG',  'ALXN',  'GR',  'MHK',  'NXPI',  'FTR',  'XL',  'MPWR',  'S',  'NYX',  'WCG',  'FANG',  'ACE',  'TDY',  'AME',  'FNM',  'VIAB',  'AGN',  'AA',  'POOL',  'MAC',  'GRMN',  'LUK',  'MJN',  'HCBK',  'PDCO',  'FRT',  'CERN',  'DPZ',  'LKQ',  'AVGO',  'MNST',  'DELL',  'FB',  'CVH',  'IGT',  'CXO',  'AVB',  'NBL',  'FTV',  'BLK',  'AYI',  'ANDV',  'ACAS',  'OGN',  'ABBV',  'DO',  'NKTR',  'IT',  'FSLR',  'TWC',  'DV',  'GT',  'LLL',  'SVU',  'SE',  'JOY',  'JDSU',  'ROST',  'CE',  'KSE',  'SII',  'M',  'EXR',  'PBCT',  'KEYS',  'WFM',  'MOLX',  'MXIM',  'NVLS',  'CLF',  'OTIS',  'DNR',  'CELG',  'WFR',  'BC',  'ANSS',  'TWTR',  'DPS',  'HII',  'LVS',  'CTVA',  'DAL',  'NOV',  'GPS',  'DFS',  'URBN',  'SNPS',  'ATI',  'AYE',  'SPLS',  'ESV',  'LM',  'ODP',  'PTV',  'KSU',  'URI',  'XTO',  'KRFT',  'SRCL',  'DD',  'TWX',  'FTNT',  'WAB',  'CEG',  'ARG',  'ADT',  'INCY',  'SGP',  'RX',  'AIV',  'GAS',  'ENPH',  'THC',  'LVLT',  'CARR',  'SIVB',  'STI',  'AKS',  'ARE',  'MPC',  'ADS',  'KHC',  'RE',  'PBI',  'RSH',  'TDC',  'EK',  'ENDP',  'FLR',  'RHT',  'XEC',  'SLE',  'JKHY',  'MMI',  'AAL',  'GM',  'TSS',  'NYT',  'LO',  'HP',  'CPGX',  'KBH',  'QTRN',  'INTU',  'REGN',  'MNK',  'NOVL',  'HRB',  'FRC',  'CRM',  'HRS',  'IDXX',  'WRB',  'EW',  'ATO',  'HOLX',  'RTN',  'CDNS',  'FOX',  'GLK',  'AVP',  'EMC',  'DISCK',  'POM',  'NE',  'ETSY',  'SNDK',  'ALGN',  'CRL']
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

    def GetSource(self, config, date, isLive):
        source = "https://www.dropbox.com/s/ksi5liwjja8fxzv/SPYChanges.csv?dl=1"
        return SubscriptionDataSource(source, SubscriptionTransportMedium.RemoteFile);

    def Reader(self, config, line, date, isLive):
        if not (line.strip() and line[0].isdigit()):
            return None
        
        data = line.split(',')
        change = SPXChange()

        try:
            change.Symbol = config.Symbol
            change.Time = datetime.strptime(data[0], '%Y-%m-%d') + timedelta(hours=10) #- timedelta(days=5)
            
            change.Value = 0
            change["Added"] = str(data[1]).split(" ")
            change["Removed"] = str(data[2]).split(" ")

        except ValueError:
            return None
        
        return change