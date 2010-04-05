{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'wxCtr_bgTemplate',
          'title':u'Ctr Data',
          'size':(713, 868),
          'statusBar':1,
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileReadCtr',
                   'label':u'ReadCtr',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileSaveCtr',
                   'label':u'SaveCtr',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileWriteHKL',
                   'label':u'WriteHKL',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuHelp',
             'label':u'&Help',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuHelpDocumentation',
                   'label':u'Documentation',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'Button', 
    'name':'CopySelParamToSet', 
    'position':(630, 308), 
    'size':(51, 25), 
    'label':'Set', 
    },

{'type':'Button', 
    'name':'CopySelParamToAll', 
    'position':(572, 308), 
    'size':(51, 25), 
    'label':'All', 
    },

{'type':'StaticText', 
    'name':'StaticText11', 
    'position':(564, 288), 
    'text':'Copy Selected Param', 
    },

{'type':'Button', 
    'name':'CopyParamsToSet', 
    'position':(628, 254), 
    'size':(51, 25), 
    'label':'Set', 
    },

{'type':'StaticText', 
    'name':'StaticText10', 
    'position':(107, 47), 
    'text':'Bad Point', 
    },

{'type':'Button', 
    'name':'ToggleBad', 
    'position':(106, 63), 
    'size':(57, -1), 
    'label':'Toggle', 
    },

{'type':'CheckBox', 
    'name':'AutoPlotCorr', 
    'position':(204, 695), 
    'label':'Auto Plot', 
    },

{'type':'StaticText', 
    'name':'StaticText9', 
    'position':(18, 665), 
    'text':'Columns =', 
    },

{'type':'TextField', 
    'name':'PlotCol', 
    'position':(85, 663), 
    'size':(34, 20), 
    'text':'2', 
    },

{'type':'StaticLine', 
    'name':'StaticLine4', 
    'position':(151, 655), 
    'size':(127, -1), 
    'layout':'horizontal', 
    },

{'type':'StaticText', 
    'name':'StaticText8', 
    'position':(573, 234), 
    'text':'Copy Parameters: ', 
    },

{'type':'Button', 
    'name':'CopyParamsToAll', 
    'position':(569, 254), 
    'size':(51, 25), 
    'label':'All', 
    },

{'type':'TextField', 
    'name':'ParamName', 
    'position':(66, 323), 
    'size':(77, 26), 
    'editable':False, 
    },

{'type':'TextArea', 
    'name':'ParamDescr', 
    'position':(16, 233), 
    'size':(542, 85), 
    'editable':False, 
    'text':'Parameter Description', 
    },

{'type':'StaticBox', 
    'name':'StaticBox6', 
    'position':(10, 212), 
    'size':(689, 146), 
    'label':'Parameters', 
    },

{'type':'Button', 
    'name':'SetUpdate', 
    'position':(244, 63), 
    'size':(57, -1), 
    'label':'Set', 
    },

{'type':'StaticText', 
    'name':'StaticText7', 
    'position':(194, 47), 
    'text':'Integrate/update', 
    },

{'type':'StaticText', 
    'name':'StaticText6', 
    'position':(154, 591), 
    'size':(131, 18), 
    'text':'Raw scan data (Fig 1)', 
    },

{'type':'StaticLine', 
    'name':'StaticLine2', 
    'position':(147, 589), 
    'size':(2, 127), 
    'layout':'horizontal', 
    },

{'type':'CheckBox', 
    'name':'AutoPlotScan', 
    'position':(204, 618), 
    'size':(73, 19), 
    'label':'Auto Plot', 
    },

{'type':'StaticText', 
    'name':'StaticText5', 
    'position':(154, 665), 
    'text':'Correction Plot (Fig 2)', 
    },

{'type':'StaticText', 
    'name':'StaticText4', 
    'position':(16, 591), 
    'text':'Ctr Plot (Fig 0)', 
    },

{'type':'Button', 
    'name':'CorrPlot', 
    'position':(157, 691), 
    'size':(42, 23), 
    'label':'Plot', 
    },

{'type':'Button', 
    'name':'ParamSet', 
    'position':(15, 322), 
    'size':(48, 27), 
    'label':'Set', 
    },

{'type':'StaticText', 
    'name':'StaticText2', 
    'position':(179, 167), 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 16}, 
    'text':'>', 
    },

{'type':'CheckBox', 
    'name':'AutoPlotIntegration', 
    'position':(151, 137), 
    'size':(149, -1), 
    'label':'Plot Integration (Fig 3)', 
    },

{'type':'Choice', 
    'name':'AnchorPointNum', 
    'position':(210, 176), 
    'size':(81, -1), 
    'items':[], 
    },

{'type':'StaticText', 
    'name':'StaticText1', 
    'position':(21, 735), 
    'text':'Add: select plane group and calculate / plot averages.  Under file we need to read / write ctr files (as hdf)', 
    },

{'type':'StaticBox', 
    'name':'StaticBox5', 
    'position':(339, 29), 
    'size':(360, 185), 
    'label':'Info', 
    },

{'type':'StaticBox', 
    'name':'StaticBox4', 
    'position':(9, 574), 
    'size':(279, 155), 
    'label':'Data Plots', 
    },

{'type':'StaticLine', 
    'name':'StaticLine3', 
    'position':(19, 108), 
    'size':(295, -1), 
    'layout':'horizontal', 
    },

{'type':'Slider', 
    'name':'ImaxSlider', 
    'position':(299, 699), 
    'size':(104, 18), 
    'labels':False, 
    'layout':'horizontal', 
    'max':100, 
    'min':0, 
    'tickFrequency':0, 
    'ticks':False, 
    'value':100, 
    },

{'type':'MultiColumnList', 
    'name':'CorrParamList', 
    'position':(348, 382), 
    'size':(343, 183), 
    'backgroundColor':(255, 255, 255), 
    'columnHeadings':['Name', 'Value'], 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 8}, 
    'items':[], 
    'maxColumns':20, 
    'rules':1, 
    },

{'type':'MultiColumnList', 
    'name':'IntParamList', 
    'position':(15, 381), 
    'size':(316, 184), 
    'backgroundColor':(255, 255, 255), 
    'columnHeadings':['Name', 'Value'], 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 8}, 
    'items':[], 
    'maxColumns':20, 
    'rules':1, 
    },

{'type':'TextArea', 
    'name':'PointData', 
    'position':(345, 49), 
    'size':(349, 158), 
    'editable':False, 
    'text':'Data Point Information\n', 
    },

{'type':'Button', 
    'name':'NextPoint', 
    'position':(56, 89), 
    'size':(35, 14), 
    'label':'>', 
    },

{'type':'Button', 
    'name':'PrevPoint', 
    'position':(20, 89), 
    'size':(35, 14), 
    'label':'<', 
    },

{'type':'StaticText', 
    'name':'colormap', 
    'position':(317, 594), 
    'text':'colormap', 
    },

{'type':'Choice', 
    'name':'ColorMap', 
    'position':(299, 615), 
    'size':(105, -1), 
    'items':[], 
    },

{'type':'Button', 
    'name':'AppendScan', 
    'position':(420, 3), 
    'size':(94, 21), 
    'label':'Append Scan', 
    },

{'type':'TextField', 
    'name':'ParamVal', 
    'position':(148, 323), 
    'size':(410, 26), 
    },

{'type':'StaticText', 
    'name':'text', 
    'position':(21, 114), 
    'size':(217, -1), 
    'text':'On point / set selection or append:', 
    'toolTip':'Provide Tdl variable hodling values', 
    },

{'type':'Button', 
    'name':'Update', 
    'position':(7, 3), 
    'size':(147, 22), 
    'label':'Update Shell Variables', 
    },

{'type':'StaticText', 
    'name':'Lbl1', 
    'position':(168, 6), 
    'text':'Ctr Data Name', 
    },

{'type':'ComboBox', 
    'name':'CtrDataVar', 
    'position':(262, 2), 
    'size':(139, -1), 
    'items':[u''], 
    },

{'type':'StaticBox', 
    'name':'StaticBox21', 
    'position':(9, 29), 
    'size':(321, 185), 
    'label':'Data point', 
    },

{'type':'StaticText', 
    'name':'Lbl11', 
    'position':(26, 47), 
    'text':'Point Index', 
    },

{'type':'ComboBox', 
    'name':'PointNum', 
    'position':(22, 65), 
    'size':(69, -1), 
    'items':[u'0'], 
    'stringSelection':'0', 
    'text':'0', 
    },

{'type':'CheckBox', 
    'name':'SetIntParams', 
    'position':(22, 161), 
    'size':(150, 20), 
    'label':'Set integration params', 
    },

{'type':'CheckBox', 
    'name':'SetCorrParams', 
    'position':(22, 187), 
    'size':(149, -1), 
    'label':'Set correction params', 
    },

{'type':'Button', 
    'name':'SetPointClick', 
    'position':(19, 685), 
    'size':(106, 20), 
    'label':'Select Point', 
    },

{'type':'StaticText', 
    'name':'Lbl3', 
    'position':(212, 158), 
    'text':'Anchor  index:', 
    },

{'type':'CheckBox', 
    'name':'AutoPlotCtr', 
    'position':(63, 615), 
    'size':(72, 15), 
    'checked':True, 
    'label':'Auto Plot', 
    },

{'type':'CheckBox', 
    'name':'AutoIntegrate', 
    'position':(22, 137), 
    'size':(109, -1), 
    'checked':True, 
    'label':'Auto Integrate', 
    },

{'type':'StaticBox', 
    'name':'StaticBox2', 
    'position':(342, 359), 
    'size':(355, 213), 
    'label':'Correction Parameters', 
    },

{'type':'Button', 
    'name':'SetPointsClick', 
    'position':(19, 705), 
    'size':(107, 20), 
    'label':'Select Set ', 
    },

{'type':'StaticText', 
    'name':'ImaxLbl', 
    'position':(310, 646), 
    'text':'Image Max =', 
    },

{'type':'TextField', 
    'name':'Imax', 
    'position':(302, 667), 
    'text':'-1', 
    },

{'type':'StaticBox', 
    'name':'StaticBox1', 
    'position':(8, 359), 
    'size':(328, 213), 
    'label':'Integration Parameters', 
    },

{'type':'Button', 
    'name':'PointUpdate', 
    'position':(184, 63), 
    'size':(57, -1), 
    'label':'Point', 
    },

{'type':'Choice', 
    'name':'AppendScanVar', 
    'position':(535, 2), 
    'size':(136, -1), 
    'items':[], 
    },

{'type':'StaticBox', 
    'name':'StaticBox3', 
    'position':(423, 572), 
    'size':(274, 154), 
    'label':'Rocking Scan Plot Params', 
    },

{'type':'Button', 
    'name':'PlotCtr', 
    'position':(16, 611), 
    'size':(42, 23), 
    'label':'Plot ', 
    },

{'type':'CheckBox', 
    'name':'CtrPlotInt', 
    'position':(16, 643), 
    'size':(114, -1), 
    'label':'Plot as Intensity', 
    },

{'type':'StaticBox', 
    'name':'box', 
    'position':(292, 574), 
    'size':(126, 153), 
    'label':'Image Plot Params', 
    },

{'type':'StaticText', 
    'name':'StaticText3', 
    'position':(456, 636), 
    'text':'X=', 
    },

{'type':'Choice', 
    'name':'XPlot', 
    'position':(486, 632), 
    'size':(183, -1), 
    'items':[], 
    },

{'type':'CheckBox', 
    'name':'XlogCheck', 
    'position':(505, 601), 
    'size':(45, -1), 
    'label':'Xlog', 
    },

{'type':'StaticText', 
    'name':'StaticText31', 
    'position':(457, 665), 
    'text':'Y=', 
    },

{'type':'Choice', 
    'name':'YPlot', 
    'position':(486, 661), 
    'size':(183, -1), 
    'items':[], 
    },

{'type':'CheckBox', 
    'name':'YlogCheck', 
    'position':(564, 599), 
    'label':'Ylog', 
    },

{'type':'StaticText', 
    'name':'StaticText311', 
    'position':(433, 694), 
    'text':'Norm=', 
    },

{'type':'Choice', 
    'name':'NormPlot', 
    'position':(486, 690), 
    'size':(183, -1), 
    'items':[], 
    },

{'type':'CheckBox', 
    'name':'HoldCheck', 
    'position':(625, 600), 
    'label':'Hold', 
    },

{'type':'Button', 
    'name':'PlotScanData', 
    'position':(157, 616), 
    'size':(42, 23), 
    'label':'Plot', 
    },

{'type':'StaticLine', 
    'name':'StaticLine1', 
    'position':(9, 762), 
    'size':(691, 6), 
    'layout':'horizontal', 
    },

] # end components
} # end background
] # end backgrounds
} }
