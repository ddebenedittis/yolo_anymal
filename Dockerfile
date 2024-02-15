FROM ultralytics/ultralytics:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN --mount=type=cache,sharing=locked,target=/var/cache/apt --mount=type=cache,sharing=locked,target=/var/lib/apt \
    apt-get update && apt-get install --no-install-recommends -qqy \
    bash-completion \
    x11-common \
    x11-utils

# # Create the same user as the host itself. (By default Docker creates the container as root, which is not recommended.)
# ARG UID=1000
# ARG GID=1000
# ARG USER=ros
# RUN addgroup --gid ${GID} ${USER} \
#  && adduser --gecos "ROS User" --disabled-password --uid ${UID} --gid ${GID} ${USER} \
#  && usermod -a -G dialout ${USER} \
#  && echo ${USER}" ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/99_aptget \
#  && chmod 0440 /etc/sudoers.d/99_aptget && chown root:root /etc/sudoers.d/99_aptget

# # Choose to run as user
# ENV USER ${USER}
# USER ${USER}

# # Change HOME environment variable
ENV HOME /home

COPY .config/entrypoint.sh /ros_entrypoint.sh
ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]