


https://github.com/user-attachments/assets/9ef74d96-3903-4589-bebc-c1fe87f4d364


Motorica retarget
=================

This is version of the [Motorica Dance Dataset](https://github.com/simonalexanderson/MotoricaDanceDataset) exported in both fbx and bvh format with a different skinned character applied.

The skinned character mesh is available in `Geno.fbx` and is free for non-commercial research use.

This dataset is compatible with:

* [lafan1-resolved](https://github.com/orangeduck/lafan1-resolved)
* [zeroeggs-retarget](https://github.com/orangeduck/zeroeggs-retarget)

For an example raylib application that can visualize this data on a skinned character check out the [GenoView](https://github.com/orangeduck/GenoView) repo.

Known Problems
==============

Be aware that the following animations have broken finger motion:

```
kthjazz_gCH_sFM_sngl_d01_007
kthjazz_gCH_sFM_sngl_d01_008
kthjazz_gCH_sFM_sngl_d01_009
kthjazz_gCH_sFM_sngl_d01_019
kthjazz_gCH_sFM_sngl_d02_005
kthjazz_gCH_sFM_sngl_d02_006
kthjazz_gCH_sFM_sngl_d02_018
kthjazz_gJZ_sFM_sngl_d01_001
kthjazz_gJZ_sFM_sngl_d01_002
kthjazz_gJZ_sFM_sngl_d01_020
kthjazz_gJZ_sFM_sngl_d01_021
kthjazz_gJZ_sFM_sngl_d02_003
kthjazz_gJZ_sFM_sngl_d02_004
kthjazz_gTP_sFM_sngl_d01_010
kthjazz_gTP_sFM_sngl_d02_014
kthjazz_gTP_sFM_sngl_d02_015
kthjazz_gTP_sFM_sngl_d02_016
kthjazz_gCH_sFM_cAll_d02_mCH_ch01_thesavoyorpheansthecharleston_005
```

And the following animations have no finger motion:

```
kthmisc_gCA_sFM_cAll_d01_mCA_ch0
kthmisc_gCA_sFM_cAll_d01_mCA_ch1
kthmisc_gCA_sFM_cAll_d01_mCA_ch2
kthmisc_gCA_sFM_cAll_d01_mCA_ch3
kthmisc_gCA_sFM_cAll_d01_mCA_ch4
kthmisc_gCA_sFM_cAll_d01_mCA_ch5
kthmisc_gCA_sFM_cAll_d01_mCA_ch6
kthmisc_gCA_sFM_cAll_d01_mCA_ch8
kthmisc_gCA_sFM_cAll_d01_mCA_ch9
kthmisc_gCA_sFM_cAll_d01_mCA_ch10
kthmisc_gCA_sFM_cAll_d01_mCA_ch13
kthmisc_gCA_sFM_cAll_d01_mCA_ch14
kthmisc_gCA_sFM_cAll_d01_mCA_ch15
kthmisc_gCA_sFM_cAll_d01_mCA_ch16
kthmisc_gCA_sFM_cAll_d01_mCA_ch17
kthmisc_gCA_sFM_cAll_d01_mCA_ch19
kthmisc_gCA_sFM_cAll_d01_mCA_ch20
kthmisc_gCA_sFM_cAll_d01_mCA_ch22
kthmisc_gCA_sFM_cAll_d01_mCA_ch24
kthmisc_gCA_sFM_cAll_d01_mCA_ch28
kthmisc_gCA_sFM_cAll_d01_mCA_ch29
kthmisc_gCA_sFM_cAll_d01_mCA_ch30
```

* There is a glitch in `kthstreet_gPO_sFM_cAll_d02_mPO_ch01_atombounce_001` at time 71.57
* There is a glitch in `kthstreet_gKR_sFM_cAll_d01_mKR5_ch05` between time 80.95 and 81.58
* The left hand is glitched in `kthstreet_gLH_sFM_cAll_d01_mLH12_ch12` between time 134.63 and 135.14
* The left hand is glitched in `kthstreet_gLH_sFM_cAll_d01_mLH3_ch03` between time 98.89 and 99.14
* The left hand is glitched in `kthstreet_gPO_sFM_cAll_d01_mPO6_ch06` between time 95.85 and 96.05
* The right leg is glitched in `kthstreet_gKR_sFM_cAll_d01_mKR1_ch01` between time 102.11 and 104.60
* The head is glitched in `kthstreet_gKR_sFM_cAll_d01_mKR5_ch05` between time 58.83 and 59.26
* The left hand is glitched in `kthstreet_gKR_sFM_cAll_d01_mKR5_ch05` between time 139.82 and 140.20
* The left hand is glitched in `kthstreet_gKR_sFM_cAll_d01_mKR5_ch05` between time 139.82 and 140.20
* The right hand is glitched in `kthstreet_gLH_sFM_cAll_d01_mLH11_ch11` between time 1.75 and 3.80

Download
========

* [BVH Data](https://theorangeduck.com/media/uploads/Geno/motorica-retarget/bvh.zip)
* [FBX Data](https://theorangeduck.com/media/uploads/Geno/motorica-retarget/fbx.zip)

License
=======

This version of the data is licensed under the [same terms](https://github.com/simonalexanderson/MotoricaDanceDataset/blob/main/LICENSE.txt) as the original dataset.

This means this data is NOT licensed for commercial use.


Citations
=========

When mentioning this database in an academic paper or other publication please cite the following publications as requested by the original repository:

```
@article{alexanderson2023listen,
  title={Listen, Denoise, Action! Audio-Driven Motion Synthesis with Diffusion Models},
  author={Alexanderson, Simon and Nagy, Rajmund and Beskow, Jonas and Henter, Gustav Eje},
  year={2023}
  issue_date={August 2023},
  publisher={ACM},
  volume={42},
  number={4},
  doi={10.1145/3592458},
  journal={ACM Trans. Graph.},
  articleno={44},
  numpages={20},
  pages={44:1--44:20}
}

@article{perez2021transflower,
  author={Valle-P{\'e}rez, Guillermo and Henter, Gustav Eje and Beskow, Jonas and Holzapfel, Andre and Oudeyer, Pierre-Yves and Alexanderson, Simon},
  title={Transflower: Probabilistic Autoregressive Dance Generation with Multimodal Attention},
  year={2021},
  issue_date={December 2021},
  publisher={ACM},
  volume={40},
  number={6},
  doi={10.1145/3478513.3480570},
  journal={ACM Trans. Graph.},
  articleno={195},
  numpages={14},
  pages={195:1--195:14}
}
```
