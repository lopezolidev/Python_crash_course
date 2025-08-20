halo_rings = [
    "Replacement 04C (Installation 09)",
    "Gamma Halo (Installation 03)",
    "Zeta Halo (Installation 07)",
    "Delta Halo (Installation 05)",
    "Alpha Halo (Installation 04)",
    "Replacement 04B (Installation 08)",
]

print(halo_rings)
# ['Replacement 04C (Installation 09)', 'Gamma Halo (Installation 03)', 'Zeta Halo (Installation 07)', 'Delta Halo (Installation 05)', 'Alpha Halo (Installation 04)', 'Replacement 04B (Installation 08)']

print(sorted(halo_rings))
# ['Alpha Halo (Installation 04)', 'Delta Halo (Installation 05)', 'Gamma Halo (Installation 03)', 'Replacement 04B (Installation 08)', 'Replacement 04C (Installation 09)', 'Zeta Halo (Installation 07)']

print(halo_rings)
# ['Replacement 04C (Installation 09)', 'Gamma Halo (Installation 03)', 'Zeta Halo (Installation 07)', 'Delta Halo (Installation 05)', 'Alpha Halo (Installation 04)', 'Replacement 04B (Installation 08)']

print(sorted(halo_rings, reverse=True))
# ['Zeta Halo (Installation 07)', 'Replacement 04C (Installation 09)', 'Replacement 04B (Installation 08)', 'Gamma Halo (Installation 03)', 'Delta Halo (Installation 05)', 'Alpha Halo (Installation 04)']

print(halo_rings)
# ['Replacement 04C (Installation 09)', 'Gamma Halo (Installation 03)', 'Zeta Halo (Installation 07)', 'Delta Halo (Installation 05)', 'Alpha Halo (Installation 04)', 'Replacement 04B (Installation 08)']


halo_rings.reverse()
print(halo_rings)
# ['Replacement 04B (Installation 08)', 'Alpha Halo (Installation 04)', 'Delta Halo (Installation 05)', 'Zeta Halo (Installation 07)', 'Gamma Halo (Installation 03)', 'Replacement 04C (Installation 09)']


halo_rings.reverse()
print(halo_rings)
# ['Replacement 04C (Installation 09)', 'Gamma Halo (Installation 03)', 'Zeta Halo (Installation 07)', 'Delta Halo (Installation 05)', 'Alpha Halo (Installation 04)', 'Replacement 04B (Installation 08)']


halo_rings.sort()
print(halo_rings)
# ['Alpha Halo (Installation 04)', 'Delta Halo (Installation 05)', 'Gamma Halo (Installation 03)', 'Replacement 04B (Installation 08)', 'Replacement 04C (Installation 09)', 'Zeta Halo (Installation 07)']


halo_rings.sort(reverse=True)
print(halo_rings)
# ['Zeta Halo (Installation 07)', 'Replacement 04C (Installation 09)', 'Replacement 04B (Installation 08)', 'Gamma Halo (Installation 03)', 'Delta Halo (Installation 05)', 'Alpha Halo (Installation 04)']

