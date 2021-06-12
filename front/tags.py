from dominate.tags import *

def module(name):
    script(f"import * as {name} from './js/{name}.js'; window.{name} = {name};", type="module")