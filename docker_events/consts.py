"""Docker objects attributes as enum"""
import enum


@enum.unique
class Type(enum.Enum):
    """Docker's object types"""
    CONTAINER = 'container'
    IMAGE = 'image'
    VOLUME = 'volume'
    NETWORK = 'network'
    DAEMON = 'daemon'
    PLUGIN = 'plugin'
    NODE = 'node'
    SERVICE = 'service'
    SECRET = 'secret'
    CONFIG = 'config'


TYPES = list(Type)


@enum.unique
class Action(enum.Enum):
    """Docker's object actions"""
    ATTACH = 'attach'
    COMMIT = 'commit'
    CONNECT = 'connect'
    COPY = 'copy'
    CREATE = 'create'
    DELETE = 'delete'
    DESTROY = 'destroy'
    DETACH = 'detach'
    DIE = 'die'
    DISCONNECT = 'disconnect'
    EXEC_CREATE = 'exec_create'
    EXEC_DETACH = 'exec_detach'
    EXEC_START = 'exec_start'
    EXEC_DIE = 'exec_die'
    EXPORT = 'export'
    HEALTH_STATUS = 'health_status'
    IMPORT = 'import'
    KILL = 'kill'
    LOAD = 'load'
    MOUNT = 'mount'
    OOM = 'oom'
    PAUSE = 'pause'
    PULL = 'pull'
    PUSH = 'push'
    PRUNE = 'prune'
    RELOAD = 'reload'
    REMOVE = 'remove'
    RENAME = 'rename'
    RESIZE = 'resize'
    RESTART = 'restart'
    SAVE = 'save'
    START = 'start'
    STOP = 'stop'
    TAG = 'tag'
    TOP = 'top'
    UNMOUNT = 'unmount'
    UNPAUSE = 'unpause'
    UNTAG = 'untag'
    UPDATE = 'update'


ACTIONS = list(Action)
