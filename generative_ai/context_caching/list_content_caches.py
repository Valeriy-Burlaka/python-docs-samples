# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

from typing import List

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")


def list_content_caches() -> List[str]:
    # [START generativeaionvertexai_gemini_get_list_of_context_caches]
    import vertexai

    from vertexai.preview import caching

    # TODO(developer): Update & uncomment line below
    # PROJECT_ID = "your-project-id"
    vertexai.init(project=PROJECT_ID, location="us-central1")

    cache_list = caching.CachedContent.list()
    # Access individual properties of a CachedContent object
    for cached_content in cache_list:
        print(f"Cache '{cached_content.name}' for model '{cached_content.model_name}'")
        print(f"Last updated at: {cached_content.update_time}")
        print(f"Expires at: {cached_content.expire_time}")
        # Example response:
        # Context cache '[CACHE_ID]' for model '[MODEL_ID]'
        # Last updated at: ...
        # Expires at: ...

    # [END generativeaionvertexai_gemini_get_list_of_context_caches]
    return [cached_content.name for cached_content in cache_list]


if __name__ == "__main__":
    list_content_caches()
