import Image from "next/image";
import { BannerMask } from "../../assets/images";
import { Filter } from "./filter";
import { Searchbar } from "./searchbar";

interface BannerProps {
  title: string;
}

export function Banner({ title }: BannerProps): JSX.Element {
  return (
    <div className="relative h-fit w-full bg-primary p-6">
      <span className="relative z-10 flex flex-col space-y-4">
        <h1 className="text-tertiary">{title}</h1>
        <Searchbar placeholder="Find Commander..." />
        <Filter />
      </span>
      <Image
        className="absolute right-0 top-0 z-0 float-right h-full w-full md:w-1/2"
        style={{ objectFit: "cover", objectPosition: "left" }}
        src={BannerMask}
        alt="eminence gaming logo"
      />
    </div>
  );
}
