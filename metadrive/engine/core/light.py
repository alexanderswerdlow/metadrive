from panda3d.core import LVector4, NodePath, DirectionalLight, AmbientLight

from metadrive.base_class.base_object import BaseObject
from metadrive.constants import CamMask


class Light(BaseObject):
    """
    It is dynamic element since it will follow the camera
    """
    def __init__(self, config):
        super(Light, self).__init__(random_seed=0)
        self.global_light = config["global_light"]
        self.direction_np = NodePath(DirectionalLight("direction light"))
        # self.light.node().setScene(self.render)

        self._node_path_list.append(self.direction_np)

        # Too large will cause the graphics card out of memory.
        if self.global_light:
            self.direction_np.node().setShadowCaster(True, 8192, 8192)
            # self.direction_np.setPos(0, 0, 50)
            # self.direction_np.lookAt(100, -30, 0)
        else:
            self.direction_np.node().setShadowCaster(True, 128, 128)

        # self.direction_np.node().showFrustum()
        # self.light.node().getLens().setNearFar(10, 100)

        self.direction_np.node().setColor(LVector4(1, 1, 1, 1))
        self.direction_np.node().setCameraMask(CamMask.Shadow)

        dlens = self.direction_np.node().getLens()
        if self.global_light:
            dlens.setFilmSize(64, 64)
        else:
            dlens.setFilmSize(16, 16)
        # dlens.setFocalLength(1)
        # dlens.setNear(3)

        self.direction_np.node().setColorTemperature(6800)
        self.direction_np.reparentTo(self.origin)

        self.ambient_np = NodePath(AmbientLight("Ambient"))
        self.ambient_np.node().setColor(LVector4(0.18, 0.2, 0.2, 1))
        # self.ambient_np.node().setColor(LVector4(0.8, 0.8, 0.8, 1))
        self.ambient_np.reparentTo(self.origin)

        self._node_path_list.append(self.ambient_np)

    def step(self, pos):
        raise DeprecationWarning("Use light.step_pos instead")

    def set_pos(self, pos):
        # if not self.global_light:
        self.direction_np.setPos(pos[0] - 100, pos[1] + 100, 120)
        self.direction_np.lookAt(pos[0], pos[1], 0)

    def reset(self, random_seed=None, *args, **kwargs):
        raise DeprecationWarning("Use light.step_pos instead")
