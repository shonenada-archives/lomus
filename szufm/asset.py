from gears.compressors import SlimItCompressor
from gears_less import LESSCompiler
from gears_clean_css import CleanCSSCompressor
from gears_coffeescript import CoffeeScriptCompiler


_compilers ={
    ".less": LESSCompiler.as_handler(),
    '.coffee': CoffeeScriptCompiler.as_handler()
}

_compressors = {
    "text/css": CleanCSSCompressor.as_handler(),
    "application/javascript": SlimItCompressor.as_handler()
}


def gears_environment(app):
    return app.extensions['gears']['environment']


def setup_compilers(app):
    env = gears_environment(app)
    for extension, compiler in _compilers.iteritems():
        env.compilers.register(extension, compiler)


def setup_compressors(app):
    env = gears_environment(app)
    if not app.config["DEBUG"] or app.config["TESTING"]:
        for mimetype, compressor in _compressors.iteritems():
            env.compressors.register(mimetype, compressor)
