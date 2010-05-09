
import os
import sys
import copy
from glob import glob
import help

helper = help.Helper()

# inherit these from python's __builtin__
_from_builtin= ('ArithmeticError', 'AssertionError', 'AttributeError',
                'BaseException', 'BufferError', 'BytesWarning',
                'DeprecationWarning', 'EOFError', 'EnvironmentError',
                'Exception', 'False', 'FloatingPointError',
                'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning',
                'IndentationError', 'IndexError', 'KeyError',
                'KeyboardInterrupt', 'LookupError', 'MemoryError',
                'NameError', 'None', 'NotImplemented',
                'NotImplementedError', 'OSError', 'OverflowError',
                'ReferenceError', 'RuntimeError', 'RuntimeWarning',
                'StandardError', 'StopIteration', 'SyntaxError',
                'SyntaxWarning', 'SystemError', 'SystemExit', 'True',
                'TypeError', 'UnboundLocalError', 'UnicodeDecodeError',
                'UnicodeEncodeError', 'UnicodeError',
                'UnicodeTranslateError', 'UnicodeWarning', 'ValueError',
                'Warning', 'ZeroDivisionError', 'abs', 'all', 'any',
                'apply', 'basestring', 'bin', 'bool', 'buffer',
                'bytearray', 'bytes', 'callable', 'chr', 'cmp', 'coerce',
                'complex', 'delattr', 'dict', 'dir', 'divmod', 'enumerate',
                'file', 'filter', 'float', 'format', 'frozenset',
                'getattr', 'hasattr', 'hash', 'hex', 'id', 'int',
                'isinstance', 'len', 'list', 'map', 'max', 'min', 
                'oct', 'open', 'ord', 'pow', 'property', 'range',
                'raw_input', 'reduce', 'repr', 'reversed', 'round', 'set',
                'setattr', 'slice', 'sorted', 'str', 'sum', 'tuple',
                'type', 'unichr', 'unicode', 'zip')

# inherit these from numpy

_from_numpy = ('pi','e', 'array','sin','cos','tan','exp','log','log10',
               'sqrt','arange', 'arccos', 'arccosh', 'arcsin', 'arcsinh',
               'arctan', 'arctan2', 'arctanh', 'argmax', 'argmin',
               'argsort', 'array', 'cosh', 'fabs', 'floor', 'floor_divide',
               'fmod', 'tanh', 'sign', 'sinh', 'identity', 'take',
               'choose', 'add', 'allclose', 'alltrue', 'around', 'asarray',
               'average', 'bitwise_and', 'bitwise_or', 'bitwise_xor',
               'ceil', 'clip', 'compress', 'concatenate', 'conjugate',
               'convolve', 'cumproduct', 'cumsum', 'diagonal', 'divide',
               'dot', 'equal', 'greater', 'greater_equal', 'hypot',
               'indices', 'invert', 'left_shift', 'less', 'less_equal',
               'logical_and', 'logical_not', 'logical_or', 'logical_xor',
               'maximum', 'minimum', 'multiply', 'negative', 'nonzero',
               'not_equal', 'ones', 'outer', 'power', 'product', 'put',
               'putmask', 'rank', 'ravel', 'remainder', 'repeat',
               'reshape', 'resize', 'right_shift', 'searchsorted', 'shape',
               'size', 'sometrue', 'sort', 'subtract', 'sum', 'swapaxes',
               'trace', 'transpose', 'true_divide', 'vdot', 'where',
               'zeros','linspace')

_numpy_renames ={'ln':'log',
                 'atan':'arctan',
                 'atan2':'arctan2',
                 'acos':'arccos',
                 'acosh':'arccosh',
                 'asin':'arcsin',
                 'asinh':'arcsinh'}
                 
##
## More builtin commands, to set up the larch language:
##
def _group(larch=None,**kw):
    """create a group"""
    try:
        g = larch.symtable.createGroup()
        for k,v in kw.items():  setattr(g,k,v)
        return g
    except:
        return None

def _showgroup(gname=None,larch=None):
    if larch is not None:
        if gname is None: gname = '_main'
        return larch.symtable.show_group(gname)

def _copy(obj,**kw):
    return copy.deepcopy(obj)

def _reload(mod,larch=None,**kw):
    """reload a module, either larch or python"""
    if larch is None: return None
    modname = None
    if mod in larch.symtable._sys.modules.values():
        for k,v in larch.symtable._sys.modules.items():
            if v == mod: modname = k
    elif mod in sys.modules.values():
        for k,v in sys.modules.items():
            if v == mod: modname = k
    elif (mod in larch.symtable._sys.modules.keys() or
          mod in sys.modules.keys()):          
        modname = mod
    
    if modname is not None:
        return larch.import_module(modname,reload=True)

def show_more(text,filename=None,writer=None,pagelength=30,prefix=''):
    """show lines of text in the style of more """
    txt = text[:]
    if isinstance(txt,str): txt = txt.split('\n')
    if len(txt) <1: return
    prompt = '== hit return for more, q to quit'
    ps = "%s (%%.2f%%%%) == " % prompt
    if filename: ps = "%s (%%.2f%%%%  of %s) == " % (prompt,filename)

    if writer is None:  writer = sys.stdout

    i = 0
    for i in range(len(txt)):
        if txt[i].endswith('\n'):
            writer.write("%s%s" % (prefix,txt[i]))
        else:
            writer.write("%s%s\n" % (prefix,txt[i]))
        i = i + 1
        if i % pagelength == 0:
            try:
                x = raw_input(ps %  (100.*i/len(txt)))
                if x in ('q','Q'): return
            except KeyboardInterrupt:
                writer.write("\n")
                return

def _ls(dir='.', **kws):
    " return list of files in the current directory "
    dir.strip()
    if len(dir) == 0: arg = '.'
    if os.path.isdir(dir):
        ret = os.listdir(dir)
    else:
        ret = glob(dir)
    if sys.platform == 'win32':
        for i, r in enumerate(ret):
            ret[i] = ret[i].replace('\\','/')
    return ret

def _ls_cmdout(x, ncol=None, **kws):
    " output for ls "
    pass # return show_list(x, ncol=ncol)

def _cwd(x=None, **kws):
    "return current working directory"
    ret = os.getcwd()
    if sys.platform == 'win32':
        ret = ret.replace('\\','/')
    return ret

def _cd(name,**kwds):
    "change directorty"
    name = name.strip()
    if name:
        os.chdir(name)

    ret = os.getcwd()
    if sys.platform == 'win32':
        ret = ret.replace('\\','/')
    return ret

def _more(name,pagelength=24,**kws):
    "list file contents"
    try:
        f = open(name)
        l = f.readlines()

    except IOError:
        print "cannot open file: %s." % name
        return
    finally:
        f.close()
    show_more(l,filename=name,pagelength=pagelength)
    
def _help(*args,**kws):
    "show help on topic or object"
    helper.buffer = []
    larch = kws.get('larch',None)
    if helper.larch is None and larch is not None:  helper.larch = larch
    if args == ('',):
        args = ('help',)
    if helper.larch is None:
        helper.addtext('cannot start help system!')
    else:
        [helper.help(a.strip()) for a in args]

    return helper.getbuffer()

def _plot(*args,**kws):
    pass

    
_local_funcs = {'group':_group,
                'showgroup':_showgroup,
                'reload':_reload,
                'copy': _copy,
                'more': _more,
                'ls': _ls,
                'cd': _cd,
                'help': _help,
                }
       
