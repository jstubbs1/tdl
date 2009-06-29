#######################################################################
"""
Tom Trainor (fftpt@uaf.edu)
Frank Heberling (Frank.Heberling@ine.fzk.de)
Matt Newville (newville@cars.uchicago.edu)

Methods to handle image processing
Reads in data for the pilatus detector
Simple integrations and plotting

Modifications:
--------------


"""
#######################################################################
"""
Todo
 - Need to improve show image / options
 - Improve plotting in integrate
 - Need non-linear backgrounds in integrate?

"""
#######################################################################
"""
Note in older versions of PIL:
 To read the pilatus, you must add this line:
    (1, 1, 1, (32,), ()): ("F", "F;32F"),
 to the OPEN_INFO dict in TiffImagePlugin.py (part of the Image module)

 starting at line 130 of TiffImagePlugin.py (from PIL 1.1.6):
   (1, 1, 2, (8,), ()): ("L", "L;R"),
   (1, 1, 1, (16,), ()): ("I;16", "I;16"),
   (1, 1, 1, (32,), ()): ("F", "F;32F"),
   (1, 2, 1, (16,), ()): ("I;16S", "I;16S"),
"""
#######################################################################

import types
import copy
import numpy as Num
import Image
import pylab

from  mathutil import LinReg
import xrf_bgr

#######################################################################
def read_files(file_prefix,start=0,end=100,nfmt=3):
    """
    read files
    """
    images  = []
    format = '%' + str(nfmt) + '.' + str(nfmt) + 'd'
    for j in range(start,end+1):
        ext  = format % j
        file = file_prefix + '_' + ext + '.tif'
        arr  = read_file(file)
        images.append(arr)
    return images

def read_file(tiff_file):
    """
    read file
    """
    try:
        im  = Image.open(tiff_file)
    except:
        print "Error reading file: %s" % tiff_file
        return Num.array([[0]])
    arr = Num.fromstring(im.tostring(), dtype='int32')
    arr.shape = im.size[1],im.size[0]
    #return arr.transpose()
    return arr

############################################################################
def image_plot(img,fig=None,figtitle='',cmap=None,verbose=False,):
    """
    show image
    
    * arguments:
       img              # the image array to be displayed
       fig = None       # Figure to plot to
       figtitle = ''    # Title
       cmap = None      # Colormap.  None uses default
                        # you can pass a string name if its in pylab.cm.colormaps
                        # or you can pass explicitly the colormap
       verbose = False  # Print some fig statistics

    * examples:
       >>>image_plot(im,fig=1,figtitle='Image',cmap='hot')
       >>>image_plot(im,fig=1,figtitle='Image',cmap=pylab.cm.Spectral)
       
    """
    if verbose:
        print '###################'
        print 'Some statistics for plotted image'
        print 'Image total= ', img.sum()
        print 'Max value = ',  img.max()
        print 'Min value = ',  img.min()
    if fig != None:
        pylab.figure(fig)
        pylab.clf()

    # pylab.imshow(img, cmap = pylab.cm.hot)
    if cmap != None:
        if type(cmap) == types.StringType:
            if cmap in pylab.cm.cmapnames:
                cmap = getattr(pylab.cm,cmap)
            else:
                cmap = None
    pylab.imshow(img,cmap=cmap)
    pylab.colorbar(orientation='horizontal')

    if figtitle:
        pylab.title(figtitle, fontsize = 12)

############################################################################
def sum_plot(image,nbgr=5,fig=None):
    #
    if fig != None:
        pylab.figure(fig)
        pylab.clf()
    else:
        pylab.figure()
    #
    pylab.subplot(211)
    pylab.title('Column Sum')
    (data, data_idx, bgr) = line_sum(image,sumflag='c',nbgr=nbgr)
    pylab.plot(data_idx, data, 'r')
    if nbgr > 0:
        pylab.plot(data_idx, bgr, 'b')
    #
    pylab.subplot(212)
    pylab.title('Row Sum')
    (data, data_idx, bgr) = line_sum(image,sumflag='r',nbgr=nbgr)
    pylab.plot(data_idx, data, 'r')
    if nbgr > 0:
        pylab.plot(data_idx, bgr, 'b')

############################################################################
def clip_image(image,roi=[],cp=False):
    """
    roi = [c1,r1,c2,r2]
    """
    if len(roi) != 4:
        roi = [0,0,image.shape[1], image.shape[0]]
    if roi[0] < roi[2]:
        c1 = roi[0]
        c2 = roi[2]
    else:
        c1 = roi[2]
        c2 = roi[0]
    if roi[1] < roi[3]:
        r1 = roi[1]
        r2 = roi[3]
    else:
        r1 = roi[3]
        r2 = roi[1]
    #(c1,r1,c2,r2) = roi
    if cp == True:
        return copy.copy(image[r1:r2, c1:c2])
    else:
        return image[r1:r2, c1:c2]

############################################################################
def line_sum(image,sumflag='c',nbgr=5):
    """
    sum down 'c'olumns or across 'r'ows
    this returns the summed data and linear background
    """
    #
    if sumflag == 'c':
        data = image.sum(axis=0)
    elif sumflag == 'r':
        data = image.sum(axis=1)
    npts     = len(data)
    data_idx = Num.arange(npts,dtype=float)
    #data_err  = data**(0.5)

    ### compute linear background
    bgr = Num.zeros(npts)
    if nbgr > 0:
        xbgr = Num.arange(0,nbgr,1,dtype=float)
        xbgr = Num.append(xbgr,Num.arange(npts-nbgr,npts,1))
        ybgr = Num.array(data[0:nbgr],dtype=float)
        ybgr = Num.append(ybgr,data[npts-nbgr:])
        lr   = LinReg(xbgr,ybgr,plot=False)
        bgr  = lr.calc_y(data_idx)
    return (data, data_idx, bgr)

############################################################################
def image_bgr(image,cwidth=100,rwidth=100,plot=False):
    """
    calculate a background for the image.
    we assume that image is already clipped
    and that it consists of a 'single peak'
    and a non-lin bgr.

    cwidth and rwidth are the 'widths' to be used
    for column and row sums respectivley. The cwidth
    value should correspond roughly to the actual peak
    width along the column direction (or the peak width in
    the row sum).  Visa versa for rrwidth.  

    Therefore the background should fit
    features that are in general broader than these values

    initially try using the xrf bgr algorithm
    if this works then we can optimize for images

    Note should change this to do either row or column sum
    only if the cwidth/rwidth are > 0.  If both are > 0
    then we should take the average.  

    """
    bgr_arr_r = Num.zeros(image.shape)
    bgr_arr_c = Num.zeros(image.shape)

    # try fit to rows
    b = xrf_bgr.Background(bottom_width=rwidth,compress=1)
    for j in range(image.shape[0]):
        b.calc(image[j])
        bgr_arr_r[j,:] = copy.copy(b.bgr)

    # try fit to cols
    #b = xrf_bgr.Background(bottom_width=cwidth,compress=1)
    b.bottom_width = cwidth
    for j in range(image.shape[1]):
        b.calc(image[:,j])
        bgr_arr_c[:,j] = copy.copy(b.bgr)

    # combine the two bgrs by average
    #bgr = (bgr_arr_r + bgr_arr_c)/2.
    # combine by taking the minimum of the two at each point
    bgr = bgr_arr_r
    idx = Num.where(bgr > bgr_arr_c)
    bgr[idx] = bgr_arr_c[idx]
    
    #show
    if plot:
        pylab.figure(1)
        pylab.clf()
        pylab.subplot(3,1,1)
        pylab.imshow(image)
        pylab.title("image")
        pylab.colorbar()

        pylab.subplot(3,1,2)
        pylab.imshow(bgr)
        pylab.title("background")
        pylab.colorbar()

        pylab.subplot(3,1,3)
        pylab.imshow(image-bgr)
        pylab.title("image - background")
        pylab.colorbar()

    return bgr

def _bgr(y,width):
    """
    calc background for a given line 
    """
    npts = len(y)
    width_s = width**2
    n       = int(2*width)
    scratch = Num.zeros(n+1)

    # loop through each point
    #for j in range(npts):
    #    idx_left = Num.max(0, j- 


################################################################################
class ImageAna:
    def __init__(self,image,roi=[],nbgr=5,cwidth=0,rwidth=0,
                 plot=True,fig=None,figtitle=''):
        """
        Note take x as the horizontal image axis index (col index), 
        and y as vertical axis index (row index).
        Therefore, in image indexing:
          image[y1:y2,x1:x2] ==> rows y1 to y2 and cols x1 to x2

        Parameters:
          * roi  = [x1,y1,x2,y2]
          * nbgr = number of bgr points
          * show_plot = show fancy plot 

        """
        ### roi = [x1,y1,x2,y2] = [c1,r1,c2,r2]
        if len(roi) < 4:
            roi = [0,0,image.shape[1], image.shape[0]]
        if roi[0] < roi[2]:
            c1 = roi[0]
            c2 = roi[2]
        else:
            c1 = roi[2]
            c2 = roi[0]
        if roi[1] < roi[3]:
            r1 = roi[1]
            r2 = roi[3]
        else:
            r1 = roi[3]
            r2 = roi[1]
        self.roi    = (int(c1),int(r1),int(c2),int(r2))
        #
        self.image  = image
        self.nbgr   = nbgr
        self.title  = figtitle
        #
        self.I      = 0.0
        self.Ibgr   = 0.0
        self.Ierr   = 0.0
        #
        self.I_c    = 0.0
        self.I_r    = 0.0
        self.Ibgr_c = 0.0
        self.Ibgr_r = 0.0
        self.Ierr_c = 0.0
        self.Ierr_r = 0.0
        #
        self.bgr_cwidth = cwidth
        self.bgr_rwidth = rwidth
        #
        self.integrate_sums()
        # plot
        if plot == True:
            self.plot(fig=fig)
            
    ############################################################################
    def integrate_sums(self):
        """
        Convert image to line plots and integrate.

        Note approx error by assuming data and bgr errors are:
           sig_i = sqrt(I_i)
        Therefore:
          (sig_Itot)**2 = Sum(I_i)
          (sig_Itot)**2 = Sum(Ibgr_i)
          Ierr = sqrt((sig_Itot)**2 + (sig_Itot)**2)
        """
        def _integrate_line(data, data_idx, bgr):
            ### integrate
            #Itot = data.sum()
            #Ibgr = bgr.sum()
            Itot = 0.0
            Ibgr = 0.0
            Itot = Num.trapz(data)
            Ibgr = Num.trapz(bgr)
            I    = Itot - Ibgr
            ### compute errors
            #Ierr = (data.sum() + bgr.sum())**(0.5)
            Ierr = (Itot + Ibgr)**(0.5)
            return(I,Ierr,Ibgr)

        # clip image
        image = clip_image(self.image,self.roi)
        nbgr = self.nbgr

        # subtract background
        if (self.bgr_cwidth > 0) or (self.bgr_rwidth > 0):
            bgr = image_bgr(image,cwidth=self.bgr_cwidth,
                            rwidth=self.bgr_rwidth)
            image = image - bgr
            #calc an error here for bgr => integral of bgr
            #then calc I as the image sum
            #self.I = Num.sum(Num.trapz(image))
            #self.Ibgr = Num.sum(Num.trapz(bgr))
            #self.Ierr = (self.I + self.Ibgr)**0.5
            #             sum of squares of I and Ibgr
            #ie doesnt make sense to
            # do row / column sums with lin bgr since we should have
            # removed all the bgr in this step.

        # Should we only do below integrations if dont do above?
        # Or we need a flag for setting how we do the integration
        
        # integrate col sum
        (data, data_idx, bgr) = line_sum(image,sumflag='c',nbgr=nbgr)
        (I,Ierr,Ibgr) = _integrate_line(data, data_idx, bgr)
        self.I_c    = I
        self.Ierr_c = Ierr
        self.Ibgr_c = Ibgr
        
        # integrate row sum
        (data, data_idx, bgr) = line_sum(image,sumflag='r',nbgr=nbgr)
        (I,Ierr,Ibgr) = _integrate_line(data, data_idx, bgr)
        self.I_r    = I
        self.Ierr_r = Ierr
        self.Ibgr_r = Ibgr

    ############################################################################
    def plot(self,fig=None):
        """
        make fancy 4-panel plot
        """
        colormap = pylab.cm.hot
        if fig != None:
            pylab.figure(fig)
            pylab.clf()
            pylab.figure(fig,figsize=[12,8])
        else:
            pylab.figure(fig,figsize=[12,8])
        title_c = 'I = %g, Ierr = %g, Ibgr = %g' % (self.I_c,self.Ierr_c,self.Ibgr_c)
        title_r = 'I = %g, Ierr = %g, Ibgr = %g' % (self.I_r,self.Ierr_r,self.Ibgr_r)
        #
        nbgr = self.nbgr
        
        # clipped image
        image = clip_image(self.image,self.roi)

        # subtract background
        if (self.bgr_cwidth > 0) and (self.bgr_rwidth > 0):
            bgr = image_bgr(image,cwidth=self.bgr_cwidth,
                            rwidth=self.bgr_rwidth)
            image = image - bgr

        # full image with roi box
        (c1,r1,c2,r2) = self.roi
        bild= copy.copy(self.image)
        bild[r1-1:r1,c1:c2] = bild.max()
        bild[r2:r2+1,c1:c2] = bild.max()
        bild[r1:r2,c1-1:c1] = bild.max()
        bild[r1:r2,c2:c2+1] = bild.max()

        # plot column sum
        pylab.subplot(221)
        pylab.title(title_c, fontsize = 12)
        (data, data_idx, bgr) = line_sum(image,sumflag='c',nbgr=nbgr)
        pylab.plot(data_idx, data, 'r')
        #pylab.plot(data_idx, bgr, 'b')
        pylab.fill_between(data_idx,bgr,data,where= data>=bgr,facecolor='green')
        pylab.fill_between(data_idx,0,bgr,facecolor='blue')
        pylab.axis([0, data_idx.max(), 0, data.max()*1.05])

        # plot full image with ROI
        pylab.subplot(222)
        pylab.title(self.title, fontsize = 12)
        pylab.imshow(bild,cmap=colormap)
        pylab.colorbar(orientation='horizontal')

        # plot zoom on image 
        pylab.subplot(223)
        pylab.imshow(image, cmap=colormap, aspect='auto')

        # plot row sum
        pylab.subplot(224)
        pylab.title(title_r, fontsize = 12)
        (data, data_idx, bgr) = line_sum(image,sumflag='r',nbgr=nbgr)
        pylab.plot(data, data_idx, 'r')
        pylab.plot(bgr, data_idx, 'b')
        #pylab.fill_between(data, data_idx,bgr, where=bgr <= data, facecolor = 'green')
        pylab.axis([0,data.max()*1.05, data_idx.max(), 0])
        pylab.xticks(rotation=-45)

################################################################################
################################################################################
if __name__ == '__main__':
    import sys
    try:
        fname = sys.argv[1]
    except:
        print 'read_pilatus  tiff file'
        sys.exit()
    a = read_file(fname)
    image_show(a)
