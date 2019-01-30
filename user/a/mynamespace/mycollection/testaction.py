# action placeholder

from ansible.plugins.action import ActionBase

class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        return dict(changed=False, source='actionfromuser')

