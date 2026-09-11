{
  # ---------------------------------------------------------------------------
  # flake.nix — môi trường của ĐỀ TÀI NÀY, khóa chặt phiên bản.
  #
  # Engineering & Research Mentoring Program (Lucero)
  #
  # Khác với `bootstrap.sh`: bootstrap *cài* công cụ lên máy, còn file này
  # *mô tả* đúng bộ công cụ mà đề tài cần. Ai clone repo và chạy `nix develop`
  # cũng nhận **đúng cùng một phiên bản** của từng công cụ — trên máy em, máy
  # bạn cùng nhóm, máy mentor, và trên máy chạy CI.
  #
  #   nix develop            # vào môi trường
  #   nix develop -c bash    # hoặc mở hẳn một shell mới
  #
  # ⚠ BẮT BUỘC COMMIT `flake.lock`. Đó mới là thứ ghim phiên bản; thiếu nó thì
  #   file này chỉ là danh sách tên công cụ, không bảo đảm gì cả.
  #
  # Lần đầu chạy sẽ tự sinh `flake.lock`. Muốn nâng phiên bản về sau:
  #   nix flake update       # rồi commit lại flake.lock kèm lý do nâng
  # ---------------------------------------------------------------------------
  description = "Môi trường đề tài — Mentoring Lucero";

  inputs = {
    # Đổi sang nhánh khác nếu cần; phiên bản thật do flake.lock quyết định.
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11";
  };

  outputs = { self, nixpkgs }:
    let
      systems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
      forAllSystems = f: nixpkgs.lib.genAttrs systems (s: f nixpkgs.legacyPackages.${s});
    in {
      devShells = forAllSystems (pkgs: {
        default = pkgs.mkShell {
          name = "mentoring-lucero";

          packages = with pkgs; [
            # --- nền chung, mọi nhánh ---
            git
            python3
            python3Packages.numpy
            python3Packages.scipy
            python3Packages.matplotlib
            python3Packages.pandas

            # --- nhánh A1–A3: mô phỏng và kiểm chứng RTL ---
            # Xóa khối này nếu đề tài không dùng RTL.
            verilog          # Icarus Verilog (iverilog, vvp)
            verilator
            gtkwave

            # --- nhánh A4–A5: tổng hợp ---
            # Dòng chảy RTL→GDSII đầy đủ dùng flake riêng của LibreLane,
            # xem SETUP-GUIDE §C6. Ở đây chỉ cần Yosys để thử nhanh.
            yosys
          ];

          shellHook = ''
            echo ""
            echo "  Môi trường đề tài — Mentoring Lucero"
            echo "  ------------------------------------"
            printf "  python  %s\n" "$(python3 --version 2>&1 | cut -d' ' -f2)"
            command -v iverilog  >/dev/null && printf "  iverilog %s\n" "$(iverilog -V 2>&1 | head -1 | awk '{print $4}')"
            command -v yosys     >/dev/null && printf "  yosys    %s\n" "$(yosys -V 2>&1 | awk '{print $2}')"
            echo ""
            echo "  Mọi phiên bản trên do flake.lock ghim — nhớ commit file đó."
            echo ""
          '';
        };
      });
    };
}
