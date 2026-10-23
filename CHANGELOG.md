# Changelog

## [1.0.0](https://github.com/hcraveiro/ha-neakasa-litterbox/compare/v1.4.3...v1.0.0) (2026-10-23)


### Features

* add "Cat appears" state to the Status sensor (SDK 0.1.9) ([7e58330](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/7e583303d4dce0c9614b243754cc3a0858b38be6))
* add native Neakasa history sensors and beta release workflow ([f263ec9](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/f263ec9fbbbd0393efa52ddbed01732f69f19b49))
* add operating-state (Status) sensor + keep entities alive mid-cycle ([b6096f5](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/b6096f53beb1c47bf3ce6b4f586583a3367e2d38))
* add operating-state sensor + keep entities alive mid-cycle ([0fae620](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/0fae620f9dd6b25fdf3d0278895fdc8f5a5d37c4))
* allow removing devices the cloud no longer reports ([7b070cc](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/7b070ccef22b7dd2a7c0ceb3f9d766b67fb72baa))
* expose cloud event completion timestamps for app-matched activity timeline ([111f987](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/111f9874e99de11d1105918380a1c66adc9ac9ad))
* **hacs:** ship the install zip with every release ([0819e1b](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/0819e1b09562b3a074c27634645638c62b6bd0b0))
* map operating_state "cat_appears" (cat inside) in the Status sensor ([00868dd](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/00868ddee1bfdda305066855e819641f89bd7b00))
* persist confirmed leveling events with measured duration ([3187960](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/318796076193b3993d11703dfadd8f14fb120bcc))
* record native leveling events and expose completion timestamps ([354f368](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/354f3685825f4a0be2b0a629d9c03317bfe613db))
* replace blueprint with Neakasa Litterbox cloud integration ([d56641d](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/d56641db5175e988afe83fdfa082e54851c53b89))


### Bug Fixes

* abort reauth and reconfigure when credentials belong to another account ([24d837b](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/24d837bcdf438fc26ef39ff53c17ac523015e9e3))
* **api:** ignore devices that are not litter boxes ([1f5c314](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/1f5c314cfdff8a823ffd161aa9ae2dcfe60f4b4d)), closes [#89](https://github.com/hcraveiro/ha-neakasa-litterbox/issues/89)
* auto-reconnect MQTT push and retry transient coordinator errors ([26dc435](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/26dc435173546ce2ee30e46391f4d4f2cb41a055))
* avoid stale level-state refresh and false completions ([a4e59a8](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/a4e59a8f6c299ceb3c51990e16f944d6bd2da3e6))
* **binary_sensor:** clear "needs cleaning" once a clean runs after the visit ([645aa9c](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/645aa9cd97c41150a764ee0b6c56708515e91f1f))
* bind the SDK session, push supervisor and coordinator to the entry lifecycle ([47b06d1](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/47b06d1a8d09ccb89cf71fb79fdc1a6191a8490e))
* **ci:** unblock hassfest, release-please and HACS validation ([af7a47c](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/af7a47c8791abc7f296d958ac488f25011db5163))
* **deps:** bump neakasa-litterbox-sdk to 0.1.12 ([03b1516](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/03b151602eccd95bec1136b23b220a19c179d4d5))
* **deps:** bump neakasa-litterbox-sdk to 0.1.12 ([a120c7a](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/a120c7ae6b35686c1a365d7ea2c3d461081c9832))
* **deps:** bump neakasa-litterbox-sdk to 0.1.2 ([d1d2c7e](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/d1d2c7ecd8ce7d76678bdb16fddd099b2ba8ecc8))
* **deps:** bump neakasa-litterbox-sdk to 0.1.3 ([9e58d4a](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/9e58d4a5ca2319786d75667f28257d87b54eb35f))
* **deps:** bump neakasa-litterbox-sdk to 0.1.6 ([088eb4a](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/088eb4abb71107a75746d82c3e55534296251635))
* **deps:** bump neakasa-litterbox-sdk to 0.1.6 ([9993daf](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/9993daf662f2c8cd16b0a7f9bd8440863153b5f5))
* **deps:** bump neakasa-litterbox-sdk to 0.2.2 ([b8dc821](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/b8dc8213bcf1a3f0ec615018e4490f3b2aef490b))
* discover EU devices via regional Aliyun gateway (SDK 0.1.11) ([717e5b7](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/717e5b73982d32ae16bdf96957653b2648fd1fd7))
* discover EU devices via regional Aliyun gateway (SDK 0.1.11) ([b430ff8](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/b430ff82698c98fbd9fab26696a3683eff2b2794))
* EU login — bump neakasa-litterbox-sdk to 0.1.10 ([735a3fc](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/735a3fc1b59f568be44a5d9fcb7aac3c2da7c0bb))
* link cat devices through via_device_id ([ff14617](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/ff14617b8dbfe59cbad9209ebe8e26f98d0338ad))
* preserve cat weight units ([fb4735b](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/fb4735b3b54e560d85187837fd4cf621217b4b27))
* reconcile leveling completion across MQTT and cloud polling (v1.4.5b1) ([#10](https://github.com/hcraveiro/ha-neakasa-litterbox/issues/10)) ([ce3b793](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/ce3b793e14e2c89071ea1b595066411aa2060de7))
* recover automatically when a cloud request times out ([3e49d9c](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/3e49d9cb23ea7c38049f0a08867d80025c702021))
* **setup:** catch all non-auth errors as ConfigEntryNotReady ([3df3dfa](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/3df3dfa53c5128c56e4ef37b4fab183b7a6a6ec5))
* **setup:** catch all non-auth errors as ConfigEntryNotReady ([cc3d52b](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/cc3d52b570fe9c4700b8fc98574656926ab6f7ea))
* sign in again when the cloud drops the session ([f7dc675](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/f7dc675108c7d0a649cbb3545d0e21aecd879fab))
* verify the MQTT broker's TLS chain ([f9725f9](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/f9725f94f7955c2ac3c0a8d779f8a37af6cf5c81))


### Miscellaneous Chores

* bump to 1.0.0 ([11f83b3](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/11f83b3acb6fa97995957507733d72285830a923))
* Dependabot weekly Mondays 09:00 BRT ([b89b089](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/b89b08908facaf02829a5396e229835645d291d9))
* **dependabot:** run weekly instead of daily ([1388e5f](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/1388e5f83cea5a3908123aebeef91664aaae9bfd))
* **dependabot:** run weekly instead of daily ([6508d6b](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/6508d6b33370afe9ade4909716be45de764d7a4e))
* **deps-dev:** Bump neakasa-litterbox-sdk in the python-deps group ([f11dfad](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/f11dfadf8671036f1a5c3aa1cffd3f5b8a800a66))
* **deps-dev:** Bump neakasa-litterbox-sdk in the python-deps group ([b47a605](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/b47a605824b131cebef430a82cf9a8cd7b53bede))
* **deps-dev:** Bump pre-commit ([edf5d65](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/edf5d652663f4aee579a1115a09a2043a149f445))
* **deps-dev:** Bump ruff in the python-deps group ([d95c0cd](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/d95c0cd290fc4fa3f67a27c687e11fd4da6a83da))
* **deps-dev:** bump ruff to 0.16.0 ([a36383e](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/a36383ee566c27ebd3255c40afca7af409bd1ace))
* **deps-dev:** Bump the python-deps group with 2 updates ([9cb2957](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/9cb29573fbc9296aab31da25e03e07d64854430b))
* **deps-dev:** Bump the python-deps group with 2 updates ([2bf9e26](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/2bf9e26395b314cdeb3ce95d376e15f484706fa9))
* **deps:** bump neakasa-litterbox-sdk to 0.1.4 ([0b3be1c](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/0b3be1ca110c59dfbfcad194b722757dc7985c14))
* **deps:** bump neakasa-litterbox-sdk to 0.1.4 ([f35643d](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/f35643d29674ba71e81df20980c7822a1659c550))
* **deps:** Bump pip from 26.1.1 to 26.1.2 ([b1c3324](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/b1c3324ff1d50935e128b35ffec07d24cdce5294))
* **deps:** Bump the python-deps group across 1 directory with 2 updates ([54bcc62](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/54bcc62259fd1e62555b59b5028dd7f04de506f4))
* **deps:** Bump the python-deps group across 1 directory with 2 updates ([3e99708](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/3e997083b243b782f453399dab03ca09ded02083))
* lower coverage gate to 90% ([#30](https://github.com/hcraveiro/ha-neakasa-litterbox/issues/30)) ([622252c](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/622252ca58f0de423b6aa7b91289bc60ddead777))
* **main:** release 1.0.0 ([b613c28](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/b613c28e1bca2b4a53cf8370463d7ee4bfcade29))
* **main:** release 1.0.0 ([91f2336](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/91f23360c3b0bc0a9673158c8a6055681315b81e))
* **main:** release 1.0.1 ([4ce1cfd](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/4ce1cfd131c0065c1b0f60004a81f853b8803aac))
* **main:** release 1.0.2 ([3e8ccd1](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/3e8ccd106c354f306724518e7b745e6850e6b54b))
* **main:** release 1.0.3 ([88bd430](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/88bd43069b68fc084e7b21d96eef94abdacaaa5a))
* **main:** release 1.0.4 ([0482152](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/0482152fe15ff20edfbe8a92c4ef209a7b2d8907))
* **main:** release 1.0.4 ([896358f](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/896358f231bfc12b69a179e58e049a31da6f0805))
* **main:** release 1.0.5 ([247a8ea](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/247a8eaa76d5128a1793bef465010791e3f7aa17))
* **main:** release 1.0.5 ([8d72a1d](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/8d72a1dcb83a08b80cc2a697ff2a5914c84fecb2))
* **main:** release 1.0.6 ([fe11bf5](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/fe11bf51c1b1a421a41d005dece9cd827c7167f9))
* **main:** release 1.0.6 ([96b1f9a](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/96b1f9a1934a499fb889e8c8d29d66da110c2a54))
* **main:** release 1.1.0 ([89d5d25](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/89d5d25255304c844fe520040fbee9890859d673))
* **main:** release 1.1.0 ([06fc960](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/06fc960653b60c55dc78147b4e2d729a4b477527))
* **main:** release 1.2.0 ([476f6cb](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/476f6cb652f73ac4fb262f85fbd6a929ca2b412d))
* **main:** release 1.2.0 ([0da7fdb](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/0da7fdb527ffa53a0c23aff1cc0b22f3117b90c2))
* **main:** release 1.2.1 ([cde0157](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/cde015788c8600b1e481292b56324d7794392d87))
* **main:** release 1.2.1 ([dcedd80](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/dcedd803f1908b759196b97db34f1e3eac41e0df))
* **main:** release 1.2.2 ([03c9e12](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/03c9e125095f0c05e498b3816d7e6ffe13357b6c))
* **main:** release 1.2.2 ([1a4af4e](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/1a4af4e65acae06c66465af7ff4203b13b553ed4))
* **main:** release 1.2.3 ([1fa61f3](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/1fa61f3f8f81eb2e2d644278065110641bdd7e84))
* **main:** release 1.2.3 ([ef70a1a](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/ef70a1a800d5cc11f3867d6fb26a02da626417ef))
* **main:** release 1.2.4 ([4c90451](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/4c90451f62eafcdf02f459ca48fc3e459f5083d8))
* **main:** release 1.3.0 ([2c19c54](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/2c19c54bf9bb7c5a72686ce6a3af85d12a41f55e))
* **main:** release 1.3.1 ([ca632db](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/ca632dbf3fd6bdd293524def7664981a665e891f))
* **main:** release 1.3.2 ([f3019aa](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/f3019aa68ecf854c14dc7ec52eed7dae9f4aa76e))
* **main:** release 1.3.3 ([4202713](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/4202713c0e1266fa4d7cb78ed59d2312817bc494))
* **main:** release 1.3.4 ([f4e342f](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/f4e342ff44ec5f9e70f8b7a3b2a8f7909b9cc678))
* **main:** release 1.4.0 ([36d5135](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/36d5135890f86ffd1473d1b1946438546abc432d))
* **main:** release 1.4.1 ([f32b32d](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/f32b32da0c17b79701bed4244c1926a9fabe71b5))
* **main:** release 1.4.2 ([8fc7b81](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/8fc7b81b366d9a15185443d8efd53cd66c0f1bb3))
* **main:** release 1.4.3 ([e4dc0c7](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/e4dc0c792f144dcf116316149db62fbe179e3865))
* move CI to the shared workflows repository ([6c40e2f](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/6c40e2f38c12cbcf3b7028a724154462a89201ef))
* prepare beta 1.4.4b4 with measured leveling duration ([30f913d](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/30f913d64534fcb68d2ac0dda6df300ff84722f7))
* prepare v1.4.4b3 leveling diagnostics beta ([525843e](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/525843e1f100d1ae76aad881b6b72204e14fe1bf))
* release on every conventional commit type ([71ee60e](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/71ee60e18a6aa0013ea0dd5e8e73991cfaa7837e))
* **release:** keep only user-facing changes in the changelog ([878d1f3](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/878d1f3f591703cb75cd95ebff691a4d3b47caac))
* repair scripts/setup and pin pre-commit hooks to the project toolchain ([92b6bef](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/92b6befe8621c604a18c8875cfe3caa382ec84ef))
* run Dependabot weekly on Mondays at 09:00 (America/Sao_Paulo) ([0ce383e](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/0ce383e3e74e4a153a4aad44755ea2c4a06f53a8))
* run lint commands directly instead of scripts/lint wrapper; fix stale CODE_STYLE.md config references ([#29](https://github.com/hcraveiro/ha-neakasa-litterbox/issues/29)) ([38603e2](https://github.com/hcraveiro/ha-neakasa-litterbox/commit/38603e2cadea2afab4b1821e3dd630ae9ec4c3a5))

## [1.4.3](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.4.2...v1.4.3) (2026-09-21)


### Bug Fixes

* **api:** ignore devices that are not litter boxes ([1f5c314](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/1f5c314cfdff8a823ffd161aa9ae2dcfe60f4b4d)), closes [#89](https://github.com/roquerodrigo/ha-neakasa-litterbox/issues/89)


### Dependencies

* **deps:** bump anyio from 4.13.0 to 4.14.2 ([710fe92](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/710fe92932de641bea5798fc7320b802b0086b4e))


### Development Dependencies

* **deps-dev:** bump ruff in the python-deps group ([4ee5328](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/4ee5328066cec2cf079de3d158dabd08928c1f77))

## [1.4.2](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.4.1...v1.4.2) (2026-09-08)


### Bug Fixes

* link cat devices through via_device_id ([ff14617](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/ff14617b8dbfe59cbad9209ebe8e26f98d0338ad))

## [1.4.1](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.4.0...v1.4.1) (2026-09-08)


### Bug Fixes

* preserve cat weight units ([fb4735b](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/fb4735b3b54e560d85187837fd4cf621217b4b27))


### Dependencies

* **deps:** bump pip from 26.1.2 to 26.2 ([e2b8b25](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/e2b8b256a6ed7802f95bdf822b6072b22748f21e))


### Development Dependencies

* **deps-dev:** bump ruff ([d0a02dc](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/d0a02dcd0bd97e4d1c6884af78c57483cbbc4d8a))


### Documentation

* add GitHub Sponsors button and support section ([2ddb367](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/2ddb3672d8d6c4c97fa11ea368f05044d33fb366))
* record the dedicated session-expired error ([54a6711](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/54a67117d5480ab88cb9f3928006aafe8d869a90))

## [1.4.0](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.3.4...v1.4.0) (2026-08-24)


### Features

* **hacs:** ship the install zip with every release ([0819e1b](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/0819e1b09562b3a074c27634645638c62b6bd0b0))


### Development Dependencies

* **deps-dev:** bump the python-deps group across 1 directory with 3 updates ([c5a555f](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/c5a555fc1a7b1a499801083517d206b3def1f364))


### Documentation

* normalize README header layout ([6ee1234](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/6ee123414c8aea61e36ef573600dbb2229629bdd))

## [1.3.4](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.3.3...v1.3.4) (2026-08-07)


### Bug Fixes

* **deps:** bump neakasa-litterbox-sdk to 0.2.2 ([b8dc821](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/b8dc8213bcf1a3f0ec615018e4490f3b2aef490b))


### Tests

* fail when the manifest and dev-group SDK pins drift ([a554c17](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/a554c173c4060d9d1456da715ccab7305397b646))

## [1.3.3](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.3.2...v1.3.3) (2026-08-07)


### Bug Fixes

* abort reauth and reconfigure when credentials belong to another account ([24d837b](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/24d837bcdf438fc26ef39ff53c17ac523015e9e3))
* bind the SDK session, push supervisor and coordinator to the entry lifecycle ([47b06d1](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/47b06d1a8d09ccb89cf71fb79fdc1a6191a8490e))


### Code Refactoring

* remove blueprint leftovers and split data and entity modules into packages ([0c24e36](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/0c24e364ed712efd24076907382a285eb6f74be0))


### Dependencies

* bump the paired Home Assistant pins to 2026.8.0 ([b30d598](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/b30d598b25ff758d69f725e4b939c90300b7c1db))


### Development Dependencies

* **deps-dev:** Bump ruff ([a216280](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/a2162804fe39b9b2d46e9820449ce760130e8d37))


### Documentation

* describe the code as it is and make quality scale claims honest ([414fdbe](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/414fdbee8e1579e2de74ac12d7201ae951365619))


### Continuous Integration

* run checks on pull requests targeting any branch ([7e46bff](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/7e46bffcc01e770429bdcd390accacaece7bc5d0))
* run code scanning on pull requests targeting any branch ([9af7732](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/9af7732600b8384644328138785bd21cc34ac1d8))


### Miscellaneous Chores

* move CI to the shared workflows repository ([6c40e2f](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/6c40e2f38c12cbcf3b7028a724154462a89201ef))
* release on every conventional commit type ([71ee60e](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/71ee60e18a6aa0013ea0dd5e8e73991cfaa7837e))
* repair scripts/setup and pin pre-commit hooks to the project toolchain ([92b6bef](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/92b6befe8621c604a18c8875cfe3caa382ec84ef))

## [1.3.2](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.3.1...v1.3.2) (2026-08-02)


### Bug Fixes

* recover automatically when a cloud request times out ([3e49d9c](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/3e49d9cb23ea7c38049f0a08867d80025c702021))

## [1.3.1](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.3.0...v1.3.1) (2026-08-02)


### Bug Fixes

* sign in again when the cloud drops the session ([f7dc675](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/f7dc675108c7d0a649cbb3545d0e21aecd879fab))

## [1.3.0](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.2.4...v1.3.0) (2026-08-01)


### Features

* allow removing devices the cloud no longer reports ([7b070cc](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/7b070ccef22b7dd2a7c0ceb3f9d766b67fb72baa))

## [1.2.4](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.2.3...v1.2.4) (2026-08-01)


### Bug Fixes

* verify the MQTT broker's TLS chain ([f9725f9](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/f9725f94f7955c2ac3c0a8d779f8a37af6cf5c81))


### Documentation

* update CLAUDE.md ([1e9f364](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/1e9f364066e5b64e9eb78763d1870b463e43c951))

## [1.2.3](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.2.2...v1.2.3) (2026-07-15)


### Bug Fixes

* **deps:** bump neakasa-litterbox-sdk to 0.1.12 ([03b1516](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/03b151602eccd95bec1136b23b220a19c179d4d5))
* **deps:** bump neakasa-litterbox-sdk to 0.1.12 ([a120c7a](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/a120c7ae6b35686c1a365d7ea2c3d461081c9832))

## [1.2.2](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.2.1...v1.2.2) (2026-06-23)


### Bug Fixes

* discover EU devices via regional Aliyun gateway (SDK 0.1.11) ([717e5b7](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/717e5b73982d32ae16bdf96957653b2648fd1fd7))
* discover EU devices via regional Aliyun gateway (SDK 0.1.11) ([b430ff8](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/b430ff82698c98fbd9fab26696a3683eff2b2794))

## [1.2.1](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.2.0...v1.2.1) (2026-06-22)


### Bug Fixes

* EU login — bump neakasa-litterbox-sdk to 0.1.10 ([735a3fc](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/735a3fc1b59f568be44a5d9fcb7aac3c2da7c0bb))

## [1.2.0](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.1.0...v1.2.0) (2026-06-01)


### Features

* add "Cat appears" state to the Status sensor (SDK 0.1.9) ([7e58330](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/7e583303d4dce0c9614b243754cc3a0858b38be6))
* map operating_state "cat_appears" (cat inside) in the Status sensor ([00868dd](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/00868ddee1bfdda305066855e819641f89bd7b00))

## [1.1.0](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.0.6...v1.1.0) (2026-06-01)


### Features

* add operating-state (Status) sensor + keep entities alive mid-cycle ([b6096f5](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/b6096f53beb1c47bf3ce6b4f586583a3367e2d38))
* add operating-state sensor + keep entities alive mid-cycle ([0fae620](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/0fae620f9dd6b25fdf3d0278895fdc8f5a5d37c4))

## [1.0.6](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.0.5...v1.0.6) (2026-06-01)


### Bug Fixes

* **deps:** bump neakasa-litterbox-sdk to 0.1.6 ([088eb4a](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/088eb4abb71107a75746d82c3e55534296251635))
* **deps:** bump neakasa-litterbox-sdk to 0.1.6 ([9993daf](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/9993daf662f2c8cd16b0a7f9bd8440863153b5f5))

## [1.0.5](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.0.4...v1.0.5) (2026-05-25)


### Documentation

* fix CI badge and drop license badge ([028bed0](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/028bed0134eb66f65bf4283ccb861c7a7ce32923))
* fix CI badge and drop license badge ([eb5748b](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/eb5748b437ae9389750d3a693b8fe23f30d2c973))

## [1.0.4](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.0.3...v1.0.4) (2026-05-24)


### Bug Fixes

* **setup:** catch all non-auth errors as ConfigEntryNotReady ([3df3dfa](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/3df3dfa53c5128c56e4ef37b4fab183b7a6a6ec5))
* **setup:** catch all non-auth errors as ConfigEntryNotReady ([cc3d52b](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/cc3d52b570fe9c4700b8fc98574656926ab6f7ea))

## [1.0.3](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.0.2...v1.0.3) (2026-05-22)


### Bug Fixes

* **binary_sensor:** clear "needs cleaning" once a clean runs after the visit ([645aa9c](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/645aa9cd97c41150a764ee0b6c56708515e91f1f))

## [1.0.2](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.0.1...v1.0.2) (2026-05-22)


### Bug Fixes

* **deps:** bump neakasa-litterbox-sdk to 0.1.3 ([9e58d4a](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/9e58d4a5ca2319786d75667f28257d87b54eb35f))

## [1.0.1](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v1.0.0...v1.0.1) (2026-05-21)


### Bug Fixes

* auto-reconnect MQTT push and retry transient coordinator errors ([26dc435](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/26dc435173546ce2ee30e46391f4d4f2cb41a055))
* **deps:** bump neakasa-litterbox-sdk to 0.1.2 ([d1d2c7e](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/d1d2c7ecd8ce7d76678bdb16fddd099b2ba8ecc8))

## [1.0.0](https://github.com/roquerodrigo/ha-neakasa-litterbox/compare/v0.1.3...v1.0.0) (2026-05-20)


### Features

* replace blueprint with Neakasa Litterbox cloud integration ([d56641d](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/d56641db5175e988afe83fdfa082e54851c53b89))


### Bug Fixes

* **ci:** unblock hassfest, release-please and HACS validation ([af7a47c](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/af7a47c8791abc7f296d958ac488f25011db5163))


### Miscellaneous Chores

* bump to 1.0.0 ([11f83b3](https://github.com/roquerodrigo/ha-neakasa-litterbox/commit/11f83b3acb6fa97995957507733d72285830a923))

## Changelog
