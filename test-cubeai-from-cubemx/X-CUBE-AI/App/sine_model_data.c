/**
  ******************************************************************************
  * @file    sine_model_data.c
  * @author  AST Embedded Analytics Research Platform
  * @date    Mon Dec 13 11:51:32 2021
  * @brief   AI Tool Automatic Code Generator for Embedded NN computing
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2021 STMicroelectronics.
  * All rights reserved.
  *
  * This software component is licensed by ST under Ultimate Liberty license
  * SLA0044, the "License"; You may not use this file except in compliance with
  * the License. You may obtain a copy of the License at:
  *                             www.st.com/SLA0044
  *
  ******************************************************************************
  */
#include "sine_model_data.h"
#include "ai_platform_interface.h"


AI_ALIGNED(32)
const ai_u64 s_sine_model_weights_array_u64[ 57 ] = {
  0x3f01ae753edd93fbU, 0xbdd4fff83e90d380U, 0x3e354285bf08031dU, 0x3e7ecafd3e780536U,
  0xbecaba64bf082d01U, 0x3ecb83373d53b661U, 0xbec8f59a3f0542d1U, 0x3e958b06be7fd72eU,
  0x3c9c49983d19efe6U, 0xbf5c7e33U, 0xbec6fa3f00000000U, 0xbf1f51e3be4ec188U,
  0x0U, 0xbebcd42c3ef0b438U, 0x3eb4ef01U, 0x3f1535fd00000000U,
  0xbf7c3cb4bf9119c8U, 0xbf4e2626bf5b7750U, 0xbece3039bf132311U, 0xbe551510be9e6138U,
  0x3cddae28bd97d380U, 0x3e7cbf6b3e1ea574U, 0x3f019bde3ec36406U, 0x3f53019e3f32921aU,
  0xcba889a558b516aaU, 0x9b55957a7689bcb7U, 0xa8b7c4a574810cc9U, 0x9cabd58a63842ca8U,
  0xb6abcbb6a4c84c9cU, 0x65bb6aa6b89ba76cU, 0xa7958ac66c68b6a6U, 0xc9c98869a657485cU,
  0xa9a8466b7c8acabbU, 0x986c68bb9a857b79U, 0xbaa5abbc7888f6c8U, 0x6c58e968868ca556U,
  0x86a6856996685889U, 0x8b9bc8b9b868175cU, 0x98db9bb7a4947aa5U, 0x6b6c556b99c75768U,
  0x3eb7d1863e0d0a5bU, 0x3eeafca03edebf5cU, 0xbe8c92293df41845U, 0x3e2cd72000000000U,
  0xbe7e9602U, 0x3ea5cd8abe7036deU, 0x3e334b5000000000U, 0x3e0bc8d2U,
  0xbf67ac81bf212abfU, 0x3fa626ed3fad82feU, 0x3e928aeabec55ff1U, 0xbf31c523bf180d02U,
  0xbf06e9dc3e6326d6U, 0xbf8712643ee38674U, 0xbf1e0481bedfd1a6U, 0x3e2bad44befc9f95U,
  0xbe850ce1U,
};



AI_API_DECLARE_BEGIN

/*!
 * @brief Get network weights array pointer as a handle ptr.
 * @ingroup sine_model_data
 * @return a ai_handle pointer to the weights array
 */
AI_DEPRECATED
AI_API_ENTRY
ai_handle ai_sine_model_data_weights_get(void)
{
  static const ai_u8* const s_sine_model_weights_map[1 + 2] = {
    AI_PTR(AI_MAGIC_MARKER),
    AI_PTR(s_sine_model_weights_array_u64),
    AI_PTR(AI_MAGIC_MARKER)
  };

  return AI_HANDLE_PTR(s_sine_model_weights_map);

}


/*!
 * @brief Get network params configuration data structure.
 * @ingroup sine_model_data
 * @return true if a valid configuration is present, false otherwise
 */
AI_API_ENTRY
ai_bool ai_sine_model_data_params_get(ai_handle network, ai_network_params* params)
{
  if (!(network && params)) return false;
  
  static ai_buffer s_sine_model_data_map_activations[AI_SINE_MODEL_DATA_ACTIVATIONS_COUNT] = {
    AI_BUFFER_OBJ_INIT(AI_BUFFER_FORMAT_U8, 1, 1, AI_SINE_MODEL_DATA_ACTIVATIONS_SIZE, 1, NULL)
  };

  const ai_buffer_array map_activations = 
    AI_BUFFER_ARRAY_OBJ_INIT(AI_FLAG_NONE, AI_SINE_MODEL_DATA_ACTIVATIONS_COUNT, s_sine_model_data_map_activations);
  
  static ai_buffer s_sine_model_data_map_weights[AI_SINE_MODEL_DATA_WEIGHTS_COUNT] = {
    AI_BUFFER_OBJ_INIT(AI_BUFFER_FORMAT_U8, 1, 1, 456, 1, s_sine_model_weights_array_u64),
    
  };

  const ai_buffer_array map_weights = 
    AI_BUFFER_ARRAY_OBJ_INIT(AI_FLAG_NONE, AI_SINE_MODEL_DATA_WEIGHTS_COUNT, s_sine_model_data_map_weights);

  return ai_platform_bind_network_params(network, params, &map_weights, &map_activations);
}


AI_API_DECLARE_END
