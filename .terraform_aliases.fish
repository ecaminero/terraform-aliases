#  Copyright 2023 Edwin.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

abbr --add tf "terraform"
abbr --add tfi "terraform init"
abbr --add tfp "terraform plan"
abbr --add tfa "terraform apply"
abbr --add tfw "terraform workspace"
abbr --add tfwl "terraform workspace list"
abbr --add tfws "terraform workspace select"
abbr --add tfwd "terraform workspace delete"
abbr --add tfwn "terraform workspace new"
abbr --add tfws "terraform workspace show"
abbr --add tfpdes "terraform plan -destroy"
abbr --add tfpref "terraform plan -refresh-only"
abbr --add tfaaa "terraform apply -auto-approve"
abbr --add tfplf "terraform plan -lock=false"
abbr --add tfalf "terraform apply -lock=false"
abbr --add tfpdeslf "terraform plan -destroy -lock=false"
abbr --add tfplfdes "terraform plan -lock=false -destroy"
abbr --add tfpreflf "terraform plan -refresh-only -lock=false"
abbr --add tfplfref "terraform plan -lock=false -refresh-only"
abbr --add tfaaalf "terraform apply -auto-approve -lock=false"
abbr --add tfalfaa "terraform apply -lock=false -auto-approve"
abbr --add tfpnoc "terraform plan -no-color"
abbr --add tfanoc "terraform apply -no-color"
abbr --add tfpdesnoc "terraform plan -destroy -no-color"
abbr --add tfprefnoc "terraform plan -refresh-only -no-color"
abbr --add tfaaanoc "terraform apply -auto-approve -no-color"
abbr --add tfplfnoc "terraform plan -lock=false -no-color"
abbr --add tfalfnoc "terraform apply -lock=false -no-color"
abbr --add tfpdeslfnoc "terraform plan -destroy -lock=false -no-color"
abbr --add tfplfdesnoc "terraform plan -lock=false -destroy -no-color"
abbr --add tfpreflfnoc "terraform plan -refresh-only -lock=false -no-color"
abbr --add tfplfrefnoc "terraform plan -lock=false -refresh-only -no-color"
abbr --add tfaaalfnoc "terraform apply -auto-approve -lock=false -no-color"
abbr --add tfalfaanoc "terraform apply -lock=false -auto-approve -no-color"
