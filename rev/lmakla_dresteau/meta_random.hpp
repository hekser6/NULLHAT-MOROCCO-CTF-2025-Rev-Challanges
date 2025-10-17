#ifndef META_RANDOM_HPP
#define META_RANDOM_HPP

#include <cstddef>

namespace snowapril {

    template <int N, int M>
    struct MetaRandom {
        static constexpr int value = static_cast<int>(
            (((static_cast<unsigned long long>(N) * 1103515245ULL + 12345ULL) / 65536ULL) % 32768ULL) % static_cast<unsigned long long>(M)
        );
    };

}

#endif
