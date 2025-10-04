from argparse import ArgumentParser

parser = ArgumentParser("frosty")
subparsers = parser.add_subparsers(dest='subparser_name')
predict_cmd = subparsers.add_parser("predict")
predict_cmd.add_argument("-T", "--temperature", type=float, help="C")
predict_cmd.add_argument("-H", "--relative_humidity", type=float, help="%")
predict_cmd.add_argument("-V", "--air_velocity", type=float, help="m/s")
predict_cmd.add_argument("-C", "--cloudiness", type=float, help="%")
predict_cmd.add_argument("-D", "--dew_point", type=float, help="C")
predict_cmd.add_argument("-R", "--raw_radiation", type=float, help="W/m^2")


def white_frost(t, h, v, c, d, r):
    # TODO: tolerence for == ?
    if t <= -1 and h >= 85 and v <= 2 and c == 0 and d <= 1 and r < -40:
        return True
    if t == -5 and h == 95 and c == 2 and r == -200:
        return True
    return False

def black_frost(t, h, v, c, d, r):
    return (
        -3 <= t <= -1.5 and 
        h < 60 and 
        v >= 2 and 
        0 <= c <= 3 
        and d <= -5 
        and r < 0
        ) # or -40???

def no_frost(t, h, v, c, d, r):
    return (
        t > 0 and
        # moderate to low RH means what?
        v > 3 and
        c >= 6 and
        d <= 0 and
        r > 0
    )

def predict(t, h, v, c, d, r):
    if white_frost(t, h, v, c, d, r): 
        return "White frost"
    if black_frost(t, h, v, c, d, r): 
        return "Black frost"
    if no_frost(t, h, v, c, d, r): 
        return "No frost"
    return "Undefined case"

def main():
    print("Hello from frosty!")
    args = parser.parse_args()
    if args.subparser_name == "predict":
        result = predict(args.T, args.H, args.V, args.C, args.D, args.R)
        print(f"predicted: {result}")
    else:
        print("TODO: open a gui or smth?")


if __name__ == "__main__":
    main()
