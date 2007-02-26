{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'wxXRF_bgTemplate',
          'title':u'XRF',
          'size':(769, 799),
          'statusBar':1,
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileReadXrf',
                   'label':u'ReadXrfFile',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileSaveScript',
                   'label':'SaveScript',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileLoadScript',
                   'label':'LoadScript',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'StaticLine', 
    'name':'StaticLine14', 
    'position':(391, 18), 
    'size':(3, 78), 
    'layout':'horizontal', 
    },

{'type':'StaticText', 
    'name':'plotParameters', 
    'position':(23, 105), 
    'font':{'style': 'bold', 'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 12}, 
    'text':u'Plot Parameters', 
    },

{'type':'StaticLine', 
    'name':'StaticLine13', 
    'position':(14, 96), 
    'size':(736, 6), 
    'layout':'horizontal', 
    },

{'type':'StaticLine', 
    'name':'StaticLine12', 
    'position':(17, 125), 
    'size':(727, -1), 
    'layout':'horizontal', 
    },

{'type':'CheckBox', 
    'name':'SetParFromSave', 
    'position':(403, 69), 
    'label':u'Set Parameters From Save On Read', 
    },

{'type':'Button', 
    'name':'RestoreSavePar', 
    'position':(672, 65), 
    'size':(53, 22), 
    'label':u'Restore', 
    },

{'type':'Button', 
    'name':'SaveSavePar', 
    'position':(609, 65), 
    'size':(52, 22), 
    'label':u'Save', 
    },

{'type':'ComboBox', 
    'name':'SaveParVar', 
    'position':(524, 32), 
    'size':(198, -1), 
    'items':[], 
    },

{'type':'StaticText', 
    'name':'saveParameters', 
    'position':(407, 37), 
    'text':u'Save Parameters =', 
    },

{'type':'StaticText', 
    'name':'dataParameters', 
    'position':(399, 104), 
    'font':{'style': 'bold', 'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 12}, 
    'text':u'Data Parameters', 
    },

{'type':'StaticLine', 
    'name':'StaticLine11', 
    'position':(538, 282), 
    'size':(2, 122), 
    'layout':'horizontal', 
    },

{'type':'StaticText', 
    'name':'putButtonsForShowRoisEtcCheckDetectors', 
    'position':(102, 229), 
    'text':u'Put buttons for show rois etc, check detectors', 
    },

{'type':'StaticText', 
    'name':'energyRange', 
    'position':(401, 226), 
    'text':u'Energy Range =', 
    },

{'type':'CheckBox', 
    'name':'CorrectData', 
    'position':(626, 139), 
    'checked':True, 
    'label':u'Correct Data', 
    },

{'type':'Button', 
    'name':'DelBgr', 
    'position':(74, 306), 
    'size':(49, 20), 
    'label':u'Delete', 
    },

{'type':'Button', 
    'name':'AddBgr', 
    'position':(24, 305), 
    'size':(46, 20), 
    'label':u'Add', 
    },

{'type':'MultiColumnList', 
    'name':'BgrParams', 
    'position':(21, 329), 
    'size':(515, 71), 
    'backgroundColor':(255, 255, 255), 
    'columnHeadings':['Det', 'Exponent', 'TopWidth', 'BottWidth', 'Tangent', 'Compress'], 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 8}, 
    'items':[], 
    'maxColumns':20, 
    'rules':1, 
    },

{'type':'Button', 
    'name':'ClearAll', 
    'position':(549, 349), 
    'size':(58, -1), 
    'label':u'ClearAll', 
    },

{'type':'Button', 
    'name':'ClearDet', 
    'position':(548, 324), 
    'size':(75, -1), 
    'label':u'ClearDetector', 
    },

{'type':'StaticLine', 
    'name':'StaticLine2', 
    'position':(17, 590), 
    'size':(735, 6), 
    'layout':'horizontal', 
    },

{'type':'Button', 
    'name':'CopyAllPkParams', 
    'position':(548, 298), 
    'size':(105, -1), 
    'label':u'CopyToAllDetectors', 
    },

{'type':'ComboBox', 
    'name':'McaTaus', 
    'position':(479, 183), 
    'size':(232, -1), 
    'items':[], 
    },

{'type':'ComboBox', 
    'name':'BadMcas', 
    'position':(478, 158), 
    'size':(232, -1), 
    'items':[], 
    },

{'type':'StaticText', 
    'name':'NumMcas', 
    'position':(404, 138), 
    'text':u'NumMcas = 0', 
    },

{'type':'TextArea', 
    'name':'Messages', 
    'position':(15, 675), 
    'size':(734, 35), 
    'editable':False, 
    'text':u'Messages', 
    },

{'type':'Slider', 
    'name':'PkFWHMSlider', 
    'position':(428, 460), 
    'size':(75, 14), 
    'labels':False, 
    'layout':'horizontal', 
    'max':100, 
    'min':0, 
    'tickFrequency':0, 
    'ticks':False, 
    'value':50, 
    },

{'type':'Slider', 
    'name':'pkAmpSlider', 
    'position':(329, 460), 
    'size':(77, 14), 
    'labels':False, 
    'layout':'horizontal', 
    'max':100, 
    'min':0, 
    'tickFrequency':0, 
    'ticks':False, 
    'value':50, 
    },

{'type':'Slider', 
    'name':'pkEnSlider', 
    'position':(239, 460), 
    'size':(77, 14), 
    'labels':False, 
    'layout':'horizontal', 
    'max':50, 
    'min':-50, 
    'tickFrequency':0, 
    'ticks':False, 
    'value':0, 
    },

{'type':'StaticLine', 
    'name':'StaticLine10', 
    'position':(15, 714), 
    'size':(740, 6), 
    'layout':'horizontal', 
    },

{'type':'CheckBox', 
    'name':'XrfLineL', 
    'position':(110, 458), 
    'size':(30, -1), 
    'checked':True, 
    'label':u'L', 
    },

{'type':'CheckBox', 
    'name':'XrfLineK', 
    'position':(78, 458), 
    'checked':True, 
    'label':u'K', 
    },

{'type':'StaticText', 
    'name':'IgnoreLbl', 
    'position':(702, 418), 
    'size':(-1, 19), 
    'text':u'Ignore', 
    },

{'type':'StaticText', 
    'name':'PkLblLbl', 
    'position':(177, 417), 
    'text':u'Label', 
    },

{'type':'TextField', 
    'name':'PkLbl', 
    'position':(152, 437), 
    'size':(76, -1), 
    },

{'type':'Button', 
    'name':'UpdateTdl', 
    'position':(18, 30), 
    'size':(88, 25), 
    'label':u'Update Variables', 
    },

{'type':'StaticLine', 
    'name':'StaticLine9', 
    'position':(10, 668), 
    'size':(745, 6), 
    'layout':'horizontal', 
    },

{'type':'ComboBox', 
    'name':'FitChiExp', 
    'position':(334, 617), 
    'size':(60, -1), 
    'items':[u'0.0', u'0.5', u'1.0'], 
    'stringSelection':u'0.0', 
    'text':u'0.0', 
    },

{'type':'ComboBox', 
    'name':'FitEnFlag', 
    'position':(254, 617), 
    'size':(60, -1), 
    'items':[u'0', u'1'], 
    'stringSelection':u'1', 
    'text':u'1', 
    },

{'type':'ComboBox', 
    'name':'FitFWHMFlag', 
    'position':(174, 616), 
    'size':(60, -1), 
    'items':[u'0', u'1'], 
    'stringSelection':u'1', 
    'text':u'1', 
    },

{'type':'StaticText', 
    'name':'FitChiExpLbl', 
    'position':(329, 597), 
    'text':u'Chi Exponent', 
    },

{'type':'StaticText', 
    'name':'FitEnergyFlagLbl', 
    'position':(254, 597), 
    'text':u'Energy Flag', 
    },

{'type':'StaticText', 
    'name':'FitFWHMFlagLbl', 
    'position':(174, 597), 
    'text':u'FWHM Flag', 
    },

{'type':'Button', 
    'name':'XrfLineDel', 
    'position':(22, 445), 
    'size':(45, 22), 
    'label':u'Delete', 
    },

{'type':'TextField', 
    'name':'PkAmpFactor', 
    'position':(632, 437), 
    'size':(64, -1), 
    },

{'type':'TextField', 
    'name':'PkFwhmFlag', 
    'position':(577, 437), 
    'size':(47, -1), 
    },

{'type':'TextField', 
    'name':'PkEnFlag', 
    'position':(517, 437), 
    'size':(49, -1), 
    },

{'type':'TextField', 
    'name':'PkFWHM', 
    'position':(422, 437), 
    'size':(82, -1), 
    },

{'type':'TextField', 
    'name':'PkAmp', 
    'position':(327, 437), 
    'size':(85, -1), 
    },

{'type':'TextField', 
    'name':'PkEn', 
    'position':(237, 437), 
    'size':(80, -1), 
    },

{'type':'CheckBox', 
    'name':'PkIgnore', 
    'position':(713, 437), 
    'size':(14, 19), 
    'label':u'CheckBox', 
    },

{'type':'StaticText', 
    'name':'AmpFactorLbl', 
    'position':(638, 406), 
    'size':(56, 29), 
    'text':u'Amplitude Factor', 
    },

{'type':'StaticText', 
    'name':'FwhmFlagLbl', 
    'position':(578, 406), 
    'size':(44, 26), 
    'text':u'FWHM Flag', 
    },

{'type':'StaticText', 
    'name':'EFlagLbl', 
    'position':(524, 406), 
    'size':(43, 28), 
    'text':u'Energy Flag', 
    },

{'type':'StaticText', 
    'name':'FwhmLbl', 
    'position':(447, 417), 
    'text':u'FWHM', 
    },

{'type':'StaticText', 
    'name':'AmpLbl', 
    'position':(342, 417), 
    'text':u'Amplitude', 
    },

{'type':'StaticText', 
    'name':'EnergyLbl', 
    'position':(257, 417), 
    'text':u'Energy', 
    },

{'type':'CheckBox', 
    'name':'XrfLineShow', 
    'position':(236, 180), 
    'size':(90, -1), 
    'label':u'Show XRF Lines', 
    },

{'type':'Button', 
    'name':'XrfLineAdd', 
    'position':(22, 420), 
    'size':(45, 22), 
    'label':u'Add', 
    },

{'type':'StaticLine', 
    'name':'StaticLine8', 
    'position':(16, 404), 
    'size':(727, -1), 
    'layout':'horizontal', 
    },

{'type':'Button', 
    'name':'BgrDefault', 
    'position':(490, 304), 
    'size':(45, 22), 
    'label':u'Default', 
    },

{'type':'StaticLine', 
    'name':'StaticLine7', 
    'position':(20, 282), 
    'size':(729, -1), 
    'layout':'horizontal', 
    },

{'type':'TextField', 
    'name':'BgrCompress', 
    'position':(429, 305), 
    'size':(55, 19), 
    'text':u'4', 
    },

{'type':'TextField', 
    'name':'BgrTangent', 
    'position':(373, 304), 
    'size':(45, 19), 
    'text':u'0', 
    },

{'type':'TextField', 
    'name':'BgrBtmWdth', 
    'position':(289, 305), 
    'size':(75, 19), 
    'text':u'4.0', 
    },

{'type':'TextField', 
    'name':'BgrTopWdth', 
    'position':(212, 305), 
    'size':(70, 19), 
    'text':u'0.0', 
    },

{'type':'TextField', 
    'name':'BgrExp', 
    'position':(130, 305), 
    'size':(75, 19), 
    'text':u'2', 
    },

{'type':'StaticText', 
    'name':'FitParamDetLbl', 
    'position':(553, 263), 
    'text':u'Detector=', 
    },

{'type':'Choice', 
    'name':'DetSelect', 
    'position':(621, 259), 
    'size':(77, -1), 
    'items':[u'0'], 
    'stringSelection':u'0', 
    },

{'type':'StaticText', 
    'name':'FittingParamsLbl', 
    'position':(22, 259), 
    'font':{'style': 'bold', 'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 12}, 
    'text':u'Fit Parameters', 
    },

{'type':'StaticText', 
    'name':'BgrCompressLbl', 
    'position':(434, 289), 
    'text':u'Compress', 
    },

{'type':'StaticText', 
    'name':'BgrTangentLbl', 
    'position':(376, 289), 
    'text':u'Tangent', 
    },

{'type':'StaticText', 
    'name':'BgrBtmWidthLbl', 
    'position':(295, 288), 
    'text':u'Bottom Width', 
    },

{'type':'StaticText', 
    'name':'BgrTopWidthLbl', 
    'position':(221, 288), 
    'text':u'Top Width', 
    },

{'type':'StaticText', 
    'name':'BgrExpLbl', 
    'position':(143, 288), 
    'text':u'Exponent', 
    },

{'type':'StaticText', 
    'name':'SetIncIncLabel', 
    'position':(301, 68), 
    'text':u'Step', 
    },

{'type':'StaticLine', 
    'name':'StaticLine6', 
    'position':(10, 10), 
    'size':(745, 7), 
    'layout':'horizontal', 
    },

{'type':'StaticLine', 
    'name':'StaticLine5', 
    'position':(750, 10), 
    'size':(5, 708), 
    'layout':'horizontal', 
    },

{'type':'StaticLine', 
    'name':'StaticLine4', 
    'position':(390, 96), 
    'size':(5, 154), 
    'layout':'horizontal', 
    },

{'type':'StaticLine', 
    'name':'StaticLine3', 
    'position':(10, 12), 
    'size':(6, 708), 
    'layout':'horizontal', 
    },

{'type':'CheckBox', 
    'name':'ComponentsCheck', 
    'position':(180, 203), 
    'size':(76, -1), 
    'label':u'Components', 
    },

{'type':'StaticText', 
    'name':'TauListLbl', 
    'position':(405, 185), 
    'text':u'McaTaus = ', 
    'toolTip':u'Provide Tdl variable holding Tau values', 
    },

{'type':'CheckBox', 
    'name':'Align', 
    'position':(573, 139), 
    'checked':True, 
    'label':u'Align', 
    },

{'type':'CheckBox', 
    'name':'Total', 
    'position':(515, 139), 
    'checked':True, 
    'label':u'Total', 
    },

{'type':'StaticText', 
    'name':'McaListLbl', 
    'position':(403, 161), 
    'text':u'Bad Mcas = ', 
    'toolTip':u'Provide Tdl variable hodling values', 
    },

{'type':'CheckBox', 
    'name':'AutoIncCheck', 
    'position':(26, 65), 
    'size':(40, 20), 
    'label':u'Scan', 
    },

{'type':'StaticText', 
    'name':'AutoIncStopLabel', 
    'position':(161, 68), 
    'text':u'Stop', 
    },

{'type':'StaticText', 
    'name':'AutoIncStartLabel', 
    'position':(74, 68), 
    'text':u'Start', 
    },

{'type':'TextField', 
    'name':'AutoIncStop', 
    'position':(191, 64), 
    'size':(43, -1), 
    'text':u'0', 
    },

{'type':'TextField', 
    'name':'AutoIncStart', 
    'position':(109, 64), 
    'size':(40, -1), 
    'text':u'0', 
    },

{'type':'StaticText', 
    'name':'ExtractLbl', 
    'position':(544, 613), 
    'text':u'Extract', 
    },

{'type':'CheckBox', 
    'name':'YerrCheck', 
    'position':(182, 181), 
    'size':(49, -1), 
    'label':u'Yerr', 
    },

{'type':'StaticLine', 
    'name':'StaticLine1', 
    'position':(10, 250), 
    'size':(741, 6), 
    'layout':'horizontal', 
    },

{'type':'CheckBox', 
    'name':'UsePrevFit', 
    'position':(299, 652), 
    'label':u'Use Prev Fit', 
    },

{'type':'ComboBox', 
    'name':'InitScanIdx', 
    'position':(224, 646), 
    'size':(60, -1), 
    'items':[u'0'], 
    'stringSelection':u'0', 
    'text':u'0', 
    },

{'type':'StaticText', 
    'name':'InitScanIdxLbl', 
    'position':(120, 651), 
    'text':u'Index for scan init', 
    },

{'type':'Button', 
    'name':'UpdateXRF', 
    'position':(549, 376), 
    'size':(73, -1), 
    'label':u'Update XRF', 
    },

{'type':'Button', 
    'name':'FitScan', 
    'position':(29, 638), 
    'size':(57, -1), 
    'label':u'Fit Scan', 
    },

{'type':'Button', 
    'name':'Fit', 
    'position':(99, 612), 
    'size':(57, -1), 
    'label':u'Fit', 
    },

{'type':'MultiColumnList', 
    'name':'PkParams', 
    'position':(19, 475), 
    'size':(727, 113), 
    'backgroundColor':(255, 255, 255), 
    'columnHeadings':['Det', 'Label', 'Energy', 'Amp', 'FWHM', 'E-Flag', 'FWHM-Flag', 'Amp-Factor', 'Ignore', 'Area'], 
    'font':{'faceName': 'Tahoma', 'family': 'sansSerif', 'size': 7}, 
    'items':[], 
    'maxColumns':20, 
    'rules':False, 
    },

{'type':'Choice', 
    'name':'XrfLine', 
    'position':(73, 435), 
    'size':(74, -1), 
    'items':[], 
    },

{'type':'CheckBox', 
    'name':'BgrCheck', 
    'position':(31, 287), 
    'checked':True, 
    'label':u'FitBackground', 
    },

{'type':'Button', 
    'name':'Calc', 
    'position':(29, 612), 
    'size':(57, -1), 
    'label':u'Calc', 
    },

{'type':'StaticText', 
    'name':'XrfLineLbl', 
    'position':(82, 417), 
    'text':u'XRF Line =', 
    },

{'type':'CheckBox', 
    'name':'HoldCheck', 
    'position':(30, 200), 
    'size':(55, -1), 
    'label':u'Hold', 
    },

{'type':'CheckBox', 
    'name':'YlogCheck', 
    'position':(114, 202), 
    'size':(38, -1), 
    'label':u'Ylog', 
    },

{'type':'CheckBox', 
    'name':'XlogCheck', 
    'position':(114, 180), 
    'size':(64, -1), 
    'label':u'Xlog', 
    },

{'type':'Button', 
    'name':'EnRange', 
    'position':(682, 220), 
    'size':(42, -1), 
    'label':u'Select', 
    },

{'type':'TextField', 
    'name':'Emax', 
    'position':(585, 222), 
    'size':(85, -1), 
    'text':u'20.0', 
    },

{'type':'StaticText', 
    'name':'EmaxLbl', 
    'position':(593, 207), 
    'text':u'Emax (keV)=', 
    },

{'type':'TextField', 
    'name':'Emin', 
    'position':(490, 222), 
    'size':(85, -1), 
    'text':u'2.0', 
    },

{'type':'StaticText', 
    'name':'EminLbl', 
    'position':(505, 207), 
    'text':u'Emin (keV)=', 
    },

{'type':'ComboBox', 
    'name':'FitFmt', 
    'position':(154, 154), 
    'size':(177, -1), 
    'items':[u'Fit', u'Fit+Bgr', u'Fit and Bgr'], 
    'stringSelection':u'Fit', 
    'text':u'Fit', 
    },

{'type':'ComboBox', 
    'name':'DataFmt', 
    'position':(155, 130), 
    'size':(176, -1), 
    'items':[u'Data', u'Data-Bgr', u'Raw Mcas: All', u'Raw Mcas Included'], 
    'text':u'Data', 
    },

{'type':'Spinner', 
    'name':'NodeInc', 
    'position':(324, 64), 
    'size':(62, -1), 
    'max':10000000, 
    'min':-1000000, 
    'value':0, 
    },

{'type':'CheckBox', 
    'name':'AutoUpdateCheck', 
    'position':(31, 180), 
    'size':(77, 12), 
    'checked':True, 
    'label':u'Auto Update', 
    },

{'type':'CheckBox', 
    'name':'FitPlotCheck', 
    'position':(86, 157), 
    'size':(39, -1), 
    'label':u'Fit', 
    },

{'type':'CheckBox', 
    'name':'DataPlotCheck', 
    'position':(85, 134), 
    'checked':True, 
    'label':u'Data', 
    },

{'type':'Button', 
    'name':'Plot', 
    'position':(23, 131), 
    'size':(41, 30), 
    'label':u'Plot', 
    },

{'type':'StaticText', 
    'name':'AutoIncIncLabel', 
    'position':(242, 68), 
    'text':u'Inc', 
    },

{'type':'TextField', 
    'name':'AutoIncInc', 
    'position':(262, 64), 
    'size':(34, -1), 
    'text':u'1', 
    },

{'type':'ComboBox', 
    'name':'NodePfx', 
    'position':(218, 35), 
    'size':(170, -1), 
    'items':[], 
    },

{'type':'ComboBox', 
    'name':'Grp', 
    'position':(109, 34), 
    'size':(103, -1), 
    'items':[], 
    },

{'type':'StaticText', 
    'name':'nodeLabel', 
    'position':(278, 19), 
    'text':u'XRF node', 
    },

{'type':'StaticText', 
    'name':'grpLabel', 
    'position':(136, 18), 
    'text':u'XRF group', 
    },

] # end components
} # end background
] # end backgrounds
} }
