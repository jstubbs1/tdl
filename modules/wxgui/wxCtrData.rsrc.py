{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'wxCtr_bgTemplate',
          'title':u'Ctr Data',
          'size':(720, 829),
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
                   'label':u'ReadCtrFile',
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
         ]
     },
         'components': [

{'type':'Button', 
    'name':'SetUpdate', 
    'position':(257, 82), 
    'size':(42, 21), 
    'label':'Set', 
    },

{'type':'StaticText', 
    'name':'StaticText7', 
    'position':(106, 85), 
    'text':'Integrate/update', 
    },

{'type':'StaticText', 
    'name':'StaticText6', 
    'position':(181, 546), 
    'text':'Raw scan data', 
    },

{'type':'StaticLine', 
    'name':'StaticLine2', 
    'position':(171, 541), 
    'size':(2, 117), 
    'layout':'horizontal', 
    },

{'type':'CheckBox', 
    'name':'AutoPlotScan', 
    'position':(184, 604), 
    'label':'Auto Plot', 
    },

{'type':'StaticText', 
    'name':'CorrParamDescr', 
    'position':(360, 241), 
    'text':'Parameter Info', 
    },

{'type':'StaticText', 
    'name':'IntParamDescr', 
    'position':(21, 241), 
    'text':'Parameter Info', 
    },

{'type':'StaticText', 
    'name':'StaticText5', 
    'position':(22, 610), 
    'text':'Correction Plot', 
    },

{'type':'StaticText', 
    'name':'StaticText4', 
    'position':(27, 542), 
    'text':'Ctr Plot', 
    },

{'type':'Button', 
    'name':'CorrPlot', 
    'position':(23, 630), 
    'size':(46, -1), 
    'label':'Plot', 
    },

{'type':'Button', 
    'name':'CorrSet', 
    'position':(349, 275), 
    'size':(47, 24), 
    'label':'Set', 
    },

{'type':'Button', 
    'name':'ParamSet', 
    'position':(18, 275), 
    'size':(44, 25), 
    'label':'Set', 
    },

{'type':'StaticText', 
    'name':'StaticText2', 
    'position':(177, 169), 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 16}, 
    'text':'>', 
    },

{'type':'CheckBox', 
    'name':'AutoPlotIntegration', 
    'position':(154, 140), 
    'label':'Auto Plot Integration', 
    },

{'type':'Choice', 
    'name':'AnchorPointNum', 
    'position':(201, 178), 
    'size':(81, -1), 
    'items':[], 
    },

{'type':'StaticText', 
    'name':'StaticText1', 
    'position':(19, 687), 
    'text':'Add: select plane group and calculate / plot averages.  Under file we need to read / write ctr files (as hdf)', 
    },

{'type':'StaticBox', 
    'name':'StaticBox5', 
    'position':(312, 31), 
    'size':(386, 183), 
    'label':'Info', 
    },

{'type':'StaticBox', 
    'name':'StaticBox4', 
    'position':(8, 522), 
    'size':(269, 148), 
    'label':'Data Plots', 
    },

{'type':'StaticLine', 
    'name':'StaticLine3', 
    'position':(17, 115), 
    'size':(271, -1), 
    'layout':'horizontal', 
    },

{'type':'Slider', 
    'name':'ImageMax', 
    'position':(300, 649), 
    'size':(104, 18), 
    'labels':False, 
    'layout':'horizontal', 
    'max':100, 
    'min':0, 
    'tickFrequency':0, 
    'ticks':False, 
    'value':50, 
    },

{'type':'MultiColumnList', 
    'name':'CorrParamList', 
    'position':(350, 303), 
    'size':(340, 219), 
    'backgroundColor':(255, 255, 255), 
    'columnHeadings':['Name', 'Value'], 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 8}, 
    'items':[], 
    'maxColumns':20, 
    'rules':1, 
    },

{'type':'MultiColumnList', 
    'name':'IntParamList', 
    'position':(14, 304), 
    'size':(315, 212), 
    'backgroundColor':(255, 255, 255), 
    'columnHeadings':['Name', 'Value'], 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 8}, 
    'items':[], 
    'maxColumns':20, 
    'rules':1, 
    },

{'type':'TextArea', 
    'name':'PointData', 
    'position':(320, 55), 
    'size':(374, 152), 
    'editable':False, 
    'text':'Data Point Information\n', 
    },

{'type':'Button', 
    'name':'NextPoint', 
    'position':(53, 86), 
    'size':(36, 19), 
    'label':'>', 
    },

{'type':'Button', 
    'name':'PrevPoint', 
    'position':(19, 86), 
    'size':(36, 19), 
    'label':'<', 
    },

{'type':'StaticText', 
    'name':'colormap', 
    'position':(317, 544), 
    'text':'colormap', 
    },

{'type':'Choice', 
    'name':'ColorMap', 
    'position':(299, 565), 
    'size':(105, -1), 
    'items':[], 
    },

{'type':'Button', 
    'name':'AppendScan', 
    'position':(420, 6), 
    'size':(94, 21), 
    'label':'Append Scan', 
    },

{'type':'TextField', 
    'name':'IntParam', 
    'position':(68, 274), 
    'size':(259, 27), 
    },

{'type':'StaticText', 
    'name':'text', 
    'position':(21, 118), 
    'size':(217, -1), 
    'text':'On point / set selection or append:', 
    'toolTip':'Provide Tdl variable hodling values', 
    },

{'type':'Button', 
    'name':'Update', 
    'position':(7, 4), 
    'size':(147, 22), 
    'label':'Update Shell Variables', 
    },

{'type':'StaticText', 
    'name':'Lbl1', 
    'position':(168, 8), 
    'text':'Ctr Data Name', 
    },

{'type':'ComboBox', 
    'name':'CtrDataVar', 
    'position':(262, 5), 
    'size':(139, -1), 
    'items':[u''], 
    },

{'type':'StaticBox', 
    'name':'StaticBox21', 
    'position':(9, 30), 
    'size':(297, 184), 
    'label':'Data point', 
    },

{'type':'StaticText', 
    'name':'Lbl11', 
    'position':(26, 45), 
    'text':'Point Index', 
    },

{'type':'ComboBox', 
    'name':'PointNum', 
    'position':(21, 62), 
    'size':(69, -1), 
    'items':[u'0'], 
    'stringSelection':'0', 
    'text':'0', 
    },

{'type':'CheckBox', 
    'name':'SetIntParams', 
    'position':(22, 163), 
    'size':(150, 20), 
    'label':'Set integration params', 
    },

{'type':'CheckBox', 
    'name':'SetCorrParams', 
    'position':(22, 189), 
    'size':(149, -1), 
    'label':'Set correction params', 
    },

{'type':'Button', 
    'name':'SetPointClick', 
    'position':(211, 55), 
    'size':(42, 21), 
    'label':'Point', 
    },

{'type':'StaticText', 
    'name':'Lbl3', 
    'position':(204, 160), 
    'text':'Anchor  index:', 
    },

{'type':'CheckBox', 
    'name':'AutoPlotCtr', 
    'position':(90, 562), 
    'size':(72, 15), 
    'checked':True, 
    'label':'Auto Plot', 
    },

{'type':'CheckBox', 
    'name':'AutoIntegrate', 
    'position':(22, 140), 
    'size':(109, -1), 
    'checked':True, 
    'label':'Auto Integrate', 
    },

{'type':'StaticBox', 
    'name':'StaticBox2', 
    'position':(342, 214), 
    'size':(355, 308), 
    'label':'Correction Parameters', 
    },

{'type':'StaticText', 
    'name':'lbl4', 
    'position':(109, 58), 
    'size':(93, -1), 
    'text':'Select from plot', 
    'toolTip':'Provide Tdl variable hodling values', 
    },

{'type':'Button', 
    'name':'SetPointsClick', 
    'position':(257, 55), 
    'size':(42, 21), 
    'label':'Set ', 
    },

{'type':'TextField', 
    'name':'CorrParam', 
    'position':(405, 275), 
    'size':(285, -1), 
    },

{'type':'StaticText', 
    'name':'ImaxLbl', 
    'position':(309, 596), 
    'text':'Image Max =', 
    },

{'type':'TextField', 
    'name':'Imax', 
    'position':(300, 617), 
    'text':'-1', 
    },

{'type':'StaticBox', 
    'name':'StaticBox1', 
    'position':(8, 214), 
    'size':(328, 308), 
    'label':'Integration Parameters', 
    },

{'type':'Button', 
    'name':'PointUpdate', 
    'position':(211, 82), 
    'size':(42, 21), 
    'label':'Point', 
    },

{'type':'Choice', 
    'name':'AppendScanVar', 
    'position':(535, 4), 
    'size':(136, -1), 
    'items':[], 
    },

{'type':'StaticBox', 
    'name':'StaticBox3', 
    'position':(423, 522), 
    'size':(274, 147), 
    'label':'Rocking Scan', 
    },

{'type':'Button', 
    'name':'PlotCtr', 
    'position':(22, 567), 
    'size':(46, -1), 
    'label':'Plot ', 
    },

{'type':'CheckBox', 
    'name':'CtrPlotInt', 
    'position':(89, 585), 
    'size':(70, -1), 
    'label':'Intensity', 
    },

{'type':'StaticBox', 
    'name':'box', 
    'position':(282, 522), 
    'size':(136, 146), 
    'label':'Image', 
    },

{'type':'StaticText', 
    'name':'StaticText3', 
    'position':(456, 586), 
    'text':'X=', 
    },

{'type':'Choice', 
    'name':'XPlot', 
    'position':(486, 582), 
    'size':(183, -1), 
    'items':[], 
    },

{'type':'CheckBox', 
    'name':'XlogCheck', 
    'position':(505, 551), 
    'size':(45, -1), 
    'label':'Xlog', 
    },

{'type':'StaticText', 
    'name':'StaticText31', 
    'position':(457, 615), 
    'text':'Y=', 
    },

{'type':'Choice', 
    'name':'YPlot', 
    'position':(486, 611), 
    'size':(183, -1), 
    'items':[], 
    },

{'type':'CheckBox', 
    'name':'YlogCheck', 
    'position':(564, 549), 
    'label':'Ylog', 
    },

{'type':'StaticText', 
    'name':'StaticText311', 
    'position':(433, 644), 
    'text':'Norm=', 
    },

{'type':'Choice', 
    'name':'NormPlot', 
    'position':(486, 640), 
    'size':(183, -1), 
    'items':[], 
    },

{'type':'CheckBox', 
    'name':'HoldCheck', 
    'position':(625, 550), 
    'label':'Hold', 
    },

{'type':'Button', 
    'name':'PlotScanData', 
    'position':(180, 569), 
    'size':(46, -1), 
    'label':'Plot', 
    },

{'type':'StaticLine', 
    'name':'StaticLine1', 
    'position':(9, 712), 
    'size':(691, 6), 
    'layout':'horizontal', 
    },

] # end components
} # end background
] # end backgrounds
} }
