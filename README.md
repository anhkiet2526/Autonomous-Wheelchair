<collision>
      <geometry>
        <sphere radius="0.06"/>
      </geometry>
    </collision>

    <inertial>
      <mass value="0.5"/>
      <inertia ixx="0.00072" ixy="0" ixz="0"
               iyy="0.00072" iyz="0" izz="0.00072"/>
    </inertial>
  </link>

  <joint name="caster_joint" type="fixed">
    <parent link="base_link"/>
    <child link="caster_wheel_link"/>
    <origin xyz="-0.25 0 -0.22" rpy="0 0 0"/>
  </joint>

  <!-- ================= IMU ================= -->

  <link name="imu_link">
    <visual>
      <geometry>
        <box size="0.04 0.04 0.02"/>
      </geometry>
      <material name="gray"/>
    </visual>
    <inertial>
      <mass value="0.05"/>
      <inertia ixx="0.00001" ixy="0" ixz="0"
               iyy="0.00001" iyz="0" izz="0.00001"/>
    </inertial>
  </link>

  <joint name="imu_joint" type="fixed">
    <parent link="base_link"/>
    <child link="imu_link"/>
    <origin xyz="0 0 0.10" rpy="0 0 0"/>
  </joint>

  <!-- ================= DEPTH CAMERA ================= -->

  <link name="camera_link">
    <visual>
      <geometry>
        <box size="0.08 0.04 0.04"/>
      </geometry>
      <material name="black"/>
    </visual>
    <inertial>
      <mass value="0.15"/>
      <inertia ixx="0.0001" ixy="0" ixz="0"
               iyy="0.0001" iyz="0" izz="0.0001"/>
    </inertial>
  </link>

  <joint name="camera_joint" type="fixed">
    <parent link="base_link"/>
    <child link="camera_link"/>
    <origin xyz="0.30 0 0.08" rpy="0 0 0"/>
  </joint>

</robot>