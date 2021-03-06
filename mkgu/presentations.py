from __future__ import absolute_import, division, print_function, unicode_literals


class Presentation(object):
    """An instance of presenting a stimulus to a system, to evoke a response.  """
    def __init__(self, stimulus):
        self.stimulus = stimulus


class Stimulus(object):
    """A Stimulus instance represents an input to a system for which data are being recorded. """
    def __init__(self):
        pass


class StimulusSet(object):
    """A StimulusSet instance represents a set of stimuli associated with a DataAssembly"""
    def __init__(self):
        pass
